"""
Convert MyST/Sphinx syntax to Python Markdown / Zensical-compatible syntax.

Run from repo root: uv run python scripts/migrate_myst.py
"""

import re
import sys
from pathlib import Path

SRC = Path("src")

# ---------------------------------------------------------------------------
# Mapping: Sphinx label → (relative path from src/, optional anchor)
# Paths are relative to src/; anchor is the slug that attr_list will set.
# ---------------------------------------------------------------------------
LABEL_MAP = {
    "gocept-net-doc":                   ("index.md", ""),
    "fcio-support":                     ("index.md", "support"),
    "firststeps":                       ("guide/tutorial/index.md", "firststeps"),
    "application-deployment-intro":     ("guide/tutorial/index.md", "application-deployment-intro"),
    "application-deployment":           ("guide/deployment/index.md", "application-deployment"),
    "api":                              ("guide/api/index.md", "api"),
    "log-method":                       ("guide/api/methods.md", "log-method"),
    "api-resource-types":               ("guide/api/types.md", "api-resource-types"),
    "api-virtual-machines":             ("guide/api/types.md", "api-virtual-machines"),
    "changelog":                        ("changes/index.md", ""),
    "support-details":                  ("support/overview.md", ""),
    "support":                          ("support/index.md", "support"),
    "screen-multiuser":                 ("support/screen-multiuser.md", ""),
    "networking":                       ("infrastructure/networking/index.md", "networking"),
    "networking-overview":              ("infrastructure/networking/networking.md", "networking-overview"),
    "logical-networks":                 ("infrastructure/networking/networking.md", "logical-networks"),
    "connecting":                       ("infrastructure/networking/connecting.md", "connecting"),
    "jumphost":                         ("infrastructure/networking/connecting.md", "jumphost"),
    "outbound":                         ("infrastructure/networking/outbound.md", "outbound"),
    "firewall":                         ("infrastructure/networking/firewall.md", "firewall"),
    "custom-firewall-rules":            ("infrastructure/networking/firewall.md", "custom-firewall-rules"),
    "infrastructure":                   ("infrastructure/index.md", ""),
    "infrastructure-storage":           ("infrastructure/storage.md", ""),
    "infrastructure-storage-block":     ("infrastructure/storage.md", "infrastructure-storage-block"),
    "infrastructure-storage-disk-layout": ("infrastructure/storage.md", "infrastructure-storage-disk-layout"),
    "infrastructure-storage-performance": ("infrastructure/storage.md", "infrastructure-storage-performance"),
    "infrastructure-storage-pool-migration": ("infrastructure/storage.md", "infrastructure-storage-pool-migration"),
    "storage-objects":                  ("infrastructure/storage.md", "storage-objects"),
    "data-centers":                     ("reference/hardware/data-centers.md", "data-centers"),
    "hardware-specs":                   ("reference/hardware/specs.md", "hardware-specs"),
    "network-security":                 ("reference/security/network.md", "network-security"),
    "data-protection":                  ("reference/security/data-protection.md", ""),
    "entry-control":                    ("reference/security/data-protection.md", "entry-control"),
    "data-at-rest-encryption":          ("reference/security/data-protection.md", "data-at-rest-encryption"),
    "access-control":                   ("reference/security/data-protection.md", "access-control"),
    "disaster-recovery":                ("reference/security/disaster-recovery.md", "disaster-recovery"),
    "backup":                           ("reference/security/backup.md", "backup"),
    "useraccounts":                     ("reference/users/index.md", "useraccounts"),
    "service-users":                    ("reference/users/index.md", "service-users"),
    "permissions":                      ("reference/users/index.md", "permissions"),
    "ssh-keygen":                       ("reference/users/ssh-keygen.md", ""),
    "ssh-keygen-linux":                 ("reference/users/ssh-keygen.md", "ssh-keygen-linux"),
    "ssh-keygen-windows":               ("reference/users/ssh-keygen.md", "ssh-keygen-windows"),
    "ssh-keygen-mac":                   ("reference/users/ssh-keygen.md", "ssh-keygen-mac"),
}


def ref_url(label: str, from_file: Path) -> str:
    """Return a relative Markdown link URL for a Sphinx label, relative to from_file."""
    if label not in LABEL_MAP:
        print(f"  WARNING: unknown label '{label}' in {from_file}", file=sys.stderr)
        return f"#{label}"
    target_rel, anchor = LABEL_MAP[label]
    target = SRC / target_rel
    # Compute relative path from from_file's directory to target
    try:
        rel = target.relative_to(SRC)
        from_dir = from_file.parent.relative_to(SRC)
        levels = len(from_dir.parts)
        prefix = "../" * levels
        url = prefix + str(rel)
    except ValueError:
        url = target_rel
    if anchor:
        url += f"#{anchor}"
    return url


# ---------------------------------------------------------------------------
# Per-file transformation
# ---------------------------------------------------------------------------

def transform(text: str, file: Path) -> str:
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # ------------------------------------------------------------------
        # 1. Standalone MyST label: (label)=  (possibly with trailing space)
        # ------------------------------------------------------------------
        m = re.match(r'^\(([a-z][a-z0-9_-]*)\)=\s*$', line)
        if m:
            label = m.group(1)
            # Look ahead: find the next non-blank line
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and re.match(r'^#{1,6} ', lines[j]):
                # Attach as attr_list ID to the heading
                heading_line = lines[j].rstrip('\n')
                # Remove any existing { } attrs to avoid duplication
                heading_line = re.sub(r'\s*\{[^}]*\}\s*$', '', heading_line)
                lines[j] = heading_line + f" {{ #{label} }}\n"
                # Skip blank lines between label and heading
                i = j
                continue  # heading will be emitted in next iteration
            else:
                # Not before a heading: emit raw HTML anchor
                out.append(f'<a id="{label}"></a>\n')
                i += 1
                continue

        # ------------------------------------------------------------------
        # 2. Fenced toctree block: ```{toctree} ... ```
        # ------------------------------------------------------------------
        if re.match(r'^```\{toctree\}', line):
            # Skip until closing ```
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                i += 1
            i += 1  # skip closing ```
            # Remove trailing blank line if present
            continue

        # ------------------------------------------------------------------
        # 3. Image directive block: ```{image} path ... ```
        # ------------------------------------------------------------------
        m = re.match(r'^```\{image\} (.+)', line)
        if m:
            img_path = m.group(1).strip()
            alt = ""
            classes = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                opt = lines[i].strip()
                if opt.startswith(":alt:"):
                    alt = opt[5:].strip()
                elif opt.startswith(":class:"):
                    classes = opt[7:].strip().split()
                i += 1
            i += 1  # skip closing ```
            attr = ""
            if classes:
                attr = "{ " + " ".join(f".{c}" for c in classes) + " }"
            out.append(f"![{alt}]({img_path}){attr}\n")
            continue

        # ------------------------------------------------------------------
        # 4. Colon-fence admonition: ::::{type} or :::{type}
        # ------------------------------------------------------------------
        m = re.match(r'^:{3,4}\{(note|warning|tip|important|caution|hint|danger|error)\}', line)
        if m:
            admon_type = m.group(1)
            fence_depth = 4 if line.startswith("::::") else 3
            fence_close = "::::" if fence_depth == 4 else ":::"
            out.append(f"!!! {admon_type}\n")
            i += 1
            while i < len(lines) and not lines[i].startswith(fence_close):
                content = lines[i]
                if content.strip():
                    out.append("    " + convert_inline_roles(content, file).lstrip())
                else:
                    out.append("\n")
                i += 1
            i += 1  # skip closing :::
            continue

        # ------------------------------------------------------------------
        # 5. Backtick-brace admonition: ```{note} or ```{warning}
        # ------------------------------------------------------------------
        m = re.match(r'^```\{(note|warning|tip|important|caution|hint|danger|error)\}', line)
        if m:
            admon_type = m.group(1)
            out.append(f"!!! {admon_type}\n")
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                content = lines[i]
                if content.strip():
                    out.append("    " + convert_inline_roles(content, file).lstrip())
                else:
                    out.append("\n")
                i += 1
            i += 1  # skip closing ```
            continue

        # ------------------------------------------------------------------
        # 6. ```{rubric} title  →  #### title
        # ------------------------------------------------------------------
        m = re.match(r'^```\{rubric\}\s*(.*)', line)
        if m:
            title = m.group(1).strip()
            out.append(f"#### {title}\n")
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                i += 1
            i += 1
            continue

        # ------------------------------------------------------------------
        # 7. ```{eval-rst}  →  remove block, emit comment
        # ------------------------------------------------------------------
        if re.match(r'^```\{eval-rst\}', line):
            out.append("<!-- eval-rst block removed during Zensical migration -->\n")
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                i += 1
            i += 1
            continue

        # ------------------------------------------------------------------
        # 8. Inline role replacements (applied to the current line)
        # ------------------------------------------------------------------
        line = convert_inline_roles(line, file)

        out.append(line)
        i += 1

    return "".join(out)


def convert_inline_roles(line: str, file: Path) -> str:
    """Replace all inline MyST roles in a line."""

    # {ref}`display text <label>`  →  [display text](url)
    def replace_ref_display(m):
        display, label = m.group(1).strip(), m.group(2).strip()
        return f"[{display}]({ref_url(label, file)})"

    line = re.sub(r'\{ref\}`([^<`]+)<([^>`]+)>`', replace_ref_display, line)

    # {ref}`label`  →  [label](url)  (display will be the label itself for now)
    def replace_ref_bare(m):
        label = m.group(1).strip()
        return f"[{label}]({ref_url(label, file)})"

    line = re.sub(r'\{ref\}`([^`]+)`', replace_ref_bare, line)

    # {doc}`display text </path>`  or  {doc}`/path`
    def replace_doc(m):
        content = m.group(1).strip()
        if "<" in content:
            dm = re.match(r'^(.*)<(.+)>$', content)
            if dm:
                display, path = dm.group(1).strip(), dm.group(2).strip()
            else:
                display, path = content, content
        else:
            display, path = content, content
        # Normalise path: strip leading /
        path = path.lstrip("/")
        if not path.endswith(".md"):
            path += ".md"
        # Compute relative URL
        from_dir = file.parent.relative_to(SRC)
        levels = len(from_dir.parts)
        prefix = "../" * levels
        url = prefix + path
        return f"[{display}]({url})"

    line = re.sub(r'\{doc\}`([^`]+)`', replace_doc, line)

    # Simple code-span roles: {file}, {command}, {program}, {code}, {manpage}
    for role in ("file", "command", "program", "code", "manpage", "port", "version"):
        line = re.sub(rf'\{{{role}\}}`([^`]+)`', r'`\1`', line)

    # {kbd}`key`  →  ++key++
    line = re.sub(r'\{kbd\}`([^`]+)`', lambda m: "++" + m.group(1) + "++", line)

    return line


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    md_files = sorted(SRC.rglob("*.md"))
    # Skip locales translations
    md_files = [f for f in md_files if "locales" not in f.parts]

    changed = 0
    for f in md_files:
        original = f.read_text(encoding="utf-8")
        converted = transform(original, f)
        if converted != original:
            f.write_text(converted, encoding="utf-8")
            print(f"  updated {f}")
            changed += 1

    print(f"\nDone. {changed}/{len(md_files)} files updated.")


if __name__ == "__main__":
    main()
