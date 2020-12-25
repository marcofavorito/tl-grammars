# Run watch -n1 make

files := docs/*.md 

all: index.html main.pdf

index.html: $(files)
	pandoc $(files) -N --bibliography=biblio.bib meta.yaml --toc -f markdown \
	  -t html --template=templates/template.html -s --css=css/pandoc.css -o $@

main.pdf: $(files)
	pandoc $(files) -N --bibliography=biblio.bib meta.yaml -f markdown \
	  -t latex+raw_tex+tex_math_dollars+citations -s --css=css/pandoc.css \
	  --template=templates/template.tex --pdf-engine=xelatex -o $@

.PHONY: clean
clean:
	latexmk -C
	-rm -fr main.pdf main.run.xml *.bbl *.blg *.nlo clean.aux clean.fdb_latexmk texput.fls
	-rm -f index.html

