#!/bin/sh
docker pull aruneko/texlive
docker run -v $(pwd):/texsrc -it --rm aruneko/texlive latexmk main
