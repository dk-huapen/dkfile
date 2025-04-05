all: jiaoyan.pdf pdfpage.pdf
pdfpage.pdf:pdfpage.tex ../../../data/report/FeederReport/6586.pdf ../../../data/report/FeederReport/6591.pdf ../../../data/report/FeederReport/1242.pdf ../../../data/report/FeederReport/1203.pdf ../../../data/report/FeederReport/6597.pdf ../../../data/report/FeederReport/6600.pdf ../../../data/report/FeederReport/757.pdf ../../../data/report/FeederReport/754.pdf ../../../data/report/FeederReport/6603.pdf ../../../data/report/FeederReport/6601.pdf ../../../data/report/FeederReport/2443.pdf ../../../data/report/FeederReport/2704.pdf ../../../data/report/FeederReport/2705.pdf ../../../data/report/FeederReport/3183.pdf ../../../data/report/FeederReport/3184.pdf ../../../data/report/FeederReport/3185.pdf ../../../data/report/FeederReport/3172.pdf ../../../data/report/FeederReport/3173.pdf ../../../data/report/FeederReport/3174.pdf ../../../data/report/FeederReport/3180.pdf ../../../data/report/FeederReport/3181.pdf ../../../data/report/FeederReport/3182.pdf ../../../data/report/FeederReport/7522.pdf ../../../data/report/FeederReport/752.pdf ../../../data/report/FeederReport/6660.pdf ../../../data/report/FeederReport/7297.pdf ../../../data/report/FeederReport/7298.pdf ../../../data/report/FeederReport/7359.pdf ../../../data/report/FeederReport/7360.pdf ../../../data/report/FeederReport/7361.pdf ../../../data/report/FeederReport/7348.pdf ../../../data/report/FeederReport/7349.pdf ../../../data/report/FeederReport/7350.pdf ../../../data/report/FeederReport/7356.pdf ../../../data/report/FeederReport/7357.pdf ../../../data/report/FeederReport/7358.pdf ../../../data/report/FeederReport/7523.pdf ../../../data/report/FeederReport/6659.pdf ../../../data/report/FeederReport/6458.pdf
	pdflatex pdfpage.tex
jiaoyan.pdf:jiaoyan.tex pdfpage.pdf
	latexmk -xelatex jiaoyan.tex
distclean:
	rm *.pdf
.PHONY:clean
clean:
	rm *.[!tp]*
