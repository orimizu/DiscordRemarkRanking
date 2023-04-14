# DiscordRemarkRanking (for Windows 10/11)
This is a script to create a ranking of the number of comments and the ranking of the used pictograms for a specified month from the discord logs.

このスクリプトは、discordのログから、指定した月の発言数ランキング、使用されている絵文字のランキングを作成するスクリプトです。

## ディレクトリ構成

```
DiscordRemarkRanking
  +-- log
  | +-- 20230410   ... サンプルとして、20230410時点のログのサンプルを入れてあります（ただし自分のログだけにシュリンクしてあります）
  | +-- yyyymmdd   ... logフォルダ下のサブフォルダの名前は自由に付けてください。私は基本的に集計している日の日付にしています
  +-- python_auto
    +-- result  .......このフォルダの下に、集計結果が格納されます
    | +-- yyyymmdd  ... このフォルダは自動的に作成されます。logフォルダのサブフォルダ名と同じ名前になります
    +-- discord_log_analysis.bat
    +-- discord_log_analysis.py
    +-- reaction_image_csv2html.py
    +-- sort_remark_ranking.py
    +-- UTF-8_BOM.txt  ... UTF-8 の BOMコードをいれたファイルです。csvファイルの先頭に無理やりBOMをくっつけるために使用しています
    +-- tmp  ......... 一時ファイルを格納するフォルダです
```


## ランキング作成手順

1. DiscordChatExporter でログをダウンロードします。

* Discordのログは、DiscordChatExporter でダウンロードすることを想定しています
  * DiscordChatExporter自体は、GitHubで公開されており、以下のURLのReadme.mdのDownloadのセクションのリンク先でダウンロードできます
  * https://github.com/Tyrrrz/DiscordChatExporter
  * ドキュメントは以下を参照してください
  * https://github.com/Tyrrrz/DiscordChatExporter/tree/master/.docs
* Discord\log の下に、yyyymmdd形式のフォルダを作成します。(例えば、20230410など)
  * 例えば、20230410フォルダの場合、以下のファイルになるようにダウンロードします。
  * Discord\log\20230410\図月つくる2022誕生日記念LIVEサーバー - Text Channels - 雑談コーナー [1015156495366762533].json

2. discord_log_analysis.bat を編集してパラメータを更新します

以下の設定例には、図月つくるさんのDiscordサーバでの設定を使用しています
図月つくるさんについての詳細は、以下の Youtubeチャネルをご覧ください

https://www.youtube.com/@tsukuruchannel

* LOG_FILENAME
  * ログのファイル名です。ファイル名は、Discordのログダウンローダがサーバ・スレッドごとに自動的に命名していますので、その名前を設定してください
  * 以下、設定例です
    * ``set LOG_FILENAME=図月つくる2022誕生日記念LIVEサーバー - Text Channels - 雑談コーナー [1015156495366762533].json``
* CHANNEL_NAME 
  * 絵文字ランキングのタイトルに表示される、Discordサーバのチャネル名を指定します
  * 以下、設定例です
    * ``set CHANNEL_NAME=図月つくるサーバー 雑談コーナー``
* LOG_SUB_DIR
  * ログ用のフォルダ名です。基本、ダウンロード日を使っています。以下のjsonファイルが存在する値に設定してください
  * DiscordRemarkRanking\log\%LOG_SUB_DIR%\図月つくる2022誕生日記念LIVEサーバー - Text Channels - 雑談コーナー [1015156495366762533].json
  * 以下、設定例です
    * ``set LOG_SUB_DIR=20230410``
* B_YEAR B_MONTH
  * 2023年3月の月間集計、サーバ開始から2023年3月末までの集計をする場合
  * B_YEAR=2023  B_MONTH=03 となります。
  * 以下、設定例です
    * ``set B_YEAR=2023``
    * ``set B_MONTH=3``
* B_M_ENG 
  * B_MONTHの英語表記を入れます Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
  * コマンドプロンプトでは、配列が使えないようなので、手動解決にぶん投げています
  * 以下、設定例です
    * ``set B_M_ENG=Mar``

3. バッチを実行します

* pythonにパスが通っているコマンドプロンプトを開きます
* DiscordRemarkRanking\python_auto フォルダに cd します
* discord_log_analysis.bat を実行します

4. 作成ファイルの確認

* DiscordRemarkRanking\python_auto\result\%LOG_SUB_DIR% に、csvファイルが２つ、htmlファイルが２つ出来ているので中身を確認してください(以下は、B_YEAR=2023  B_MONTH=3  B_M_ENG=Mar で設定したときの例です）
  * reaction_emoji_ranking_20230401.html
  * reaction_emoji_ranking_2023Mar.html
  * remark_ranking_20230401.csv
  * remark_ranking_2023Mar.csv

csvは、excelで直接開けます
もしくは、google スプレッドシートでimport可能です

