# 2018年LOCAL学生部で出典する技術書用リポジトリ

## Re:View
Re:VIEW は，EWB や RD あるいは Wiki に似た簡易フォーマットで記述したテキストファイルを，目的に応じて各種の形式に変換するツールセット．

#### 環境構築
http://magicbullet.hatenablog.jp/entry/review_howtouse

#### Re:View記法
https://github.com/kmuto/review/blob/master/doc/format.ja.md

または，sample-bookディレクトリ参照

#### Re:View -> LaTeXへの変換
``` bash
review-compile --target=latex
```

#### 組版(Re:View -> PDFにタイプセット)
``` bash
review-pdfmaker config.yml
```
デフォルトはbook.pdfにタイプセットされる．
ちなみにreview-compile --target=latexで生成したtexファイルを変更しても
review-pdfmakerに反映される．

#### markdown -> Re:Viewへの変換

##### インストール
``` bash
gem install md2review
```

##### 実行
``` bash
md2review sample.md > sample.re
```

##### 変換の際の注意点
https://qiita.com/nanbuwks/items/9b00e8012e328de6e440
