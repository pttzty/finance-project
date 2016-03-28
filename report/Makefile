TITLE=finance

all:
	pdflatex $(TITLE).tex
	bibtex $(TITLE)
	pdflatex $(TITLE).tex
	pdflatex $(TITLE).tex


clean:
	rm *.aux
	rm *.log
	rm *.out
	rm *.blg
	rm *.bbl
