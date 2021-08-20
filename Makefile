PATH          := ./bin:${PATH}
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = flyingcircus
SOURCEDIR     = src
ROOTDIR       = _build
BUILDDIR      = $(ROOTDIR)/en

$(warning $(PATH) $(origin PATH))

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile html-de update-translations all

update-translations: gettext
	./bin/sphinx-intl -c src/conf.py update -l de -p _build/gettext

html-de: SPHINXOPTS+="-Dlanguage=de"
html-de: BUILDDIR="$(ROOTDIR)/de"
html-de: html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
