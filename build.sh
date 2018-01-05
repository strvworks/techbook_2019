md2review chikuwait.md > chikuwait.re
docker run --rm -v `pwd`:/User/yukinakata/Desktop/techbookfest_localstudents_2017 vvakame/review /bin/sh -c "cd /User/yukinakata/Desktop/techbookfest_localstudents_2017 && review-pdfmaker config.yml"
open book.pdf
