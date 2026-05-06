"""
Generate translated Markdown source tree (src-de/) from src/ + .po files.

This script applies the German gettext translations from
src/locales/de/LC_MESSAGES/**/*.po to the corresponding source .md files
and writes the translated output to src-de/.

Usage: uv run python scripts/apply_translations.py
"""

import re
import shutil
from pathlib import Path

import polib

SRC = Path("src")
OUT = Path("src-de")
LOCALE_DIR = SRC / "locales" / "de" / "LC_MESSAGES"


def load_po(po_path: Path) -> dict[str, str]:
    """Return msgid → msgstr mapping for translated entries."""
    catalog = polib.pofile(str(po_path))
    return {entry.msgid: entry.msgstr for entry in catalog if entry.msgstr}


def get_po_path(md_path: Path) -> Path | None:
    """Return the .po file corresponding to a source .md file, if it exists."""
    rel = md_path.relative_to(SRC).with_suffix(".po")
    po = LOCALE_DIR / rel
    return po if po.exists() else None


def apply_translations(text: str, translations: dict[str, str]) -> str:
    """Replace paragraphs and sentences that have translations."""
    # Split on blank lines to get paragraphs; try to match whole paragraphs first.
    # This is a best-effort approach; Sphinx gettext works at the paragraph level.
    paragraphs = re.split(r'(\n{2,})', text)
    result = []
    for part in paragraphs:
        stripped = part.strip()
        if stripped in translations:
            # Replace with translated text, preserving surrounding newlines
            leading = part[: len(part) - len(part.lstrip("\n"))]
            trailing = part[len(part.rstrip("\n")) :]
            result.append(leading + translations[stripped] + trailing)
        else:
            result.append(part)
    return "".join(result)


def main() -> None:
    try:
        import polib  # noqa: F401
    except ImportError:
        print("polib not installed — run: uv add --dev polib")
        raise SystemExit(1)

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT, ignore=shutil.ignore_patterns("locales", "conf.py"))

    md_files = sorted(SRC.rglob("*.md"))
    md_files = [f for f in md_files if "locales" not in f.parts]

    translated = 0
    for md_path in md_files:
        po_path = get_po_path(md_path)
        if po_path is None:
            continue
        translations = load_po(po_path)
        if not translations:
            continue
        original = md_path.read_text(encoding="utf-8")
        converted = apply_translations(original, translations)
        if converted != original:
            out_path = OUT / md_path.relative_to(SRC)
            out_path.write_text(converted, encoding="utf-8")
            translated += 1

    print(f"Translated {translated} files into {OUT}/")


if __name__ == "__main__":
    main()
