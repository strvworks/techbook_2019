$latex            = 'uplatex -synctex=1 -halt-on-error -shell-escape';
$latex_silent     = 'uplatex -synctex=1 -halt-on-error -interaction=batchmode -s
hell-escape';
$bibtex           = 'pbibtex %O %B';
$dvipdf           = 'dvipdfmx -I 24 %O -o %D %S';
$makeindex        = 'mendex %O -o %D %S';
$pdf_mode         = 3;
