# filename-replacer
 
# 概要
指定したディレクトリ下の全てのファイルのファイル名に含まれる指定した文字列を置換します。<br>
サブディレクトリ下のファイルも全て置換対象になります。<br><br>

# 動作確認環境
* Python 3.9.0
* Mac OS 10.15.7
<br><br>

# 使い方
念のためファイルのバックアップを取ってから実行してください。<br>
```
python3 filename-replacer.py ファイル名置換するディレクトリパス 置換する文字列 置換後文字列
```
<br>

例: ディレクトリ「sample」内のファイル名の「ab」を「XY」にしたいとき
```
python3 filename-replacer.py test ab XY
```
