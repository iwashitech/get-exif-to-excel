# Jpeg画像一覧のExif情報、幅・高さ、RGB/CMYK、アスペクト比、拡張子が大文字かを取得しExcelで書き出し

- Pythonだけで処理しようとすると国、都道府県、市区町村などのデータが取得できない

## ImageMagick

- [コンソール上でImageMagickを使って画像ファイルのEXIF情報を取得する](https://orebibou.com/2017/08/%E3%82%B3%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%AB%E4%B8%8A%E3%81%A7imagemagick%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E7%94%BB%E5%83%8F%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEexif%E6%83%85%E5%A0%B1/)
- [[ImageMagick] 画像の大きさ（幅と高さのピクセル数）を取得するコマンド](http://dqn.sakusakutto.jp/2009/02/imagemagick.html)
- [Identify profile-icc with Image Magick](https://stackoverflow.com/questions/5778851/identify-profile-icc-with-image-magick#answer-5778956)

## シェル

- [grepコマンドの -A -B オプション](https://qiita.com/Konboi@github/items/68e30513183ddca1f9c6)
- [grepでAND検索とOR検索](https://qiita.com/ritukiii/items/968f17f9c308743e85a7)
- [-aを付けないと、Binary file (standard input) matches エラーが出るので注意](https://qiita.com/tamadon/items/756e9281bd3cb3108368)
- [シェルスクリプトの中でjoin()とsplit()相当の事をやる](https://qiita.com/piroor/items/55ff672cb9f8e375e659)
- [行頭と行末の空白の削除 メモ](https://knaka20blue.hatenablog.com/entry/20120629/1340975155)
- [sed 正規表現を利用した文字列置換](https://bi.biopapyrus.jp/os/linux/sed.html)
- [画像からExifの読取り削除するコマンドあれこれ](https://ameblo.jp/itboy/entry-11044330647.html)
- [シェルスクリプトのif文の条件式で「command not found」となるやりがちなミスに気をつけよう](https://utano.jp/entry/2016/07/shell-script-condition-command-not-found/)
- [シェルスクリプト(bash)のif文とtestコマンド([])自分メモ](https://qiita.com/toshihirock/items/461da0f60f975f6acb10)
- [【sed / awk / grep】文字列の置換・抽出・検索と正規表現 | Linux Cheat Sheet](https://qiita.com/shuntaro_tamura/items/e4e942e7186934fae5e7)
- [sedコマンドでスペース（空白）を削除する](https://ex1.m-yabe.com/archives/3306)
- [Linux ファイルの文字コード確認・変換](https://qiita.com/H_Neco/items/48fa2eaaa0d9af2e45fe)
- [ファイルの文字コード＆改行コードを確認・変換するためのツールまとめ](https://dev.classmethod.jp/tool/character-code-and-line-feed-code-converting-tools-matome/#linux-iconv-command)

## Python

- [リスト内包表記のネスト](https://www.lifewithpython.com/2014/09/python-list-comprehension-and-generator-expression-and-dict-comprehension.html)
- [【Python】リスト内包表記 x 多重ループ](https://chuckwebtips.hatenablog.com/entry/2016/06/01/000000)
- [アスペクト比算出メモ](https://www.tsuyukimakoto.com/blog/2009/04/20/calculate_aspect_ratio/)

## Pandas

- [pandasでcsvファイルの書き出し・追記（to_csv）](https://note.nkmk.me/python-pandas-to-csv/)
- [ループ処理で値を更新する@1行ずつ取り出すDataFrame.iterrows()メソッド](https://note.nkmk.me/python-pandas-dataframe-for-iteration/#_2)
- [add a row at top in pandas dataframe](https://stackoverflow.com/questions/43408621/add-a-row-at-top-in-pandas-dataframe#answer-43408736)