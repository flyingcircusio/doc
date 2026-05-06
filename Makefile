PATH    := .venv/bin:${PATH}
SOURCEDIR = src

.PHONY: html html-de update-translations gettext all

html:
	uv run zensical build

html-de:
	uv run python scripts/apply_translations.py
	ZENSICAL_DOCS_DIR=src-de ZENSICAL_SITE_DIR=_build/de uv run zensical build

update-translations: gettext
	uv run sphinx-intl -c src/conf.py update -l de -p _build/en/gettext

gettext:
	uv run sphinx-build -b gettext $(SOURCEDIR) _build/en/gettext
