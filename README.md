# 2017年度LOCAL学生部総大会
## ファイル名
* それぞれファイル名はTwitterのID名+.tex
  * keisuke495500.tex
  * chikuwa_IT.tex
  * materialofmouse.tex
  * lrf141.tex
  * takuzoo3868.tex
  * Jumpaku.tex
## コンパイル
texlive2017をインストールしてる人は
``` bash
uplatex -shell-escape main.tex
```
それ以外の人は
``` bash
./do_latexmk.sh
```
3GBくらいのdocker imageをダウンロードするので注意


##### FujiwaLaTeXさんのfork元のmasterと同期
```bash
git remote add upstream https://github.com/username/hogehoge.git
git fetch upstream
git checkout
git merge upstream/master
```
