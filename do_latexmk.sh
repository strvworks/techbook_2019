#!/bin/sh
docker run -d -v `pwd`:/data --rm --name localst_techbook2017_latexmk aruneko/texlive \
/bin/sh -c 'cd data && \
latexmk -e \
'"'"'$dvipdf = "dvipdfmx %O -o %D %S" ;$bibtex = "pbibtex %O %B";$makeindex = "mendex %O -o %D %S";'"'"' \
-g -pdfdvi -latex=uplatex -latexoption="-shell-escape" -interaction=nonstopmode -pvc main.tex'
