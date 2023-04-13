## ディレクトリ構成

```
DiscordRemarkRanking
  +-- log
  | +-- 20230410
  | +-- yyyymmdd
  +-- python_auto
    +-- result
    | +-- 20230410
    +-- discord_log_analysis.bat
    +-- discord_log_analysis.py
    +-- reaction_image_csv2html.py
    +-- sort_remark_ranking.py
    +-- UTF-8_BOM.txt
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

* LOG_SUB_DIR
  * ログ用のフォルダ名です。基本、ダウンロード日を使っています。以下のjsonファイルが存在する値に設定してください
  * DiscordRemarkRanking\log\%LOG_SUB_DIR%\図月つくる2022誕生日記念LIVEサーバー - Text Channels - 雑談コーナー [1015156495366762533].json
  * 以下、設定例です
    * set LOG_SUB_DIR=20230410
* B_YEAR B_MONTH
  * 2023年3月の月間集計、サーバ開始から2023年3月末までの集計をする場合
  * B_YEAR=2023  B_MONTH=03 となります。
  * 以下、設定例です
    * set B_YEAR=2023
    * set B_MONTH=3
* B_M_ENG 
  * B_MONTHの英語表記を入れます Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
  * コマンドプロンプトでは、配列が使えないようなので、手動解決にぶん投げています
  * 以下、設定例です
    * set B_M_ENG=Mar

3. バッチを実行します

* pythonにパスが通っているコマンドプロンプトを開きます
* Discord\python_auto フォルダに cd します
* discord_log_analysis.bat を実行します

4. 作成ファイルの確認

* DiscordRemarkRanking\python_auto\result\%LOG_SUB_DIR% に、csvファイルが２つ、htmlファイルが２つ出来ているので中身を確認してください(以下は、B_YEAR=2023  B_MONTH=3  B_M_ENG=Mar で設定したときの例です）
  * reaction_emoji_ranking_20230401.html
  * reaction_emoji_ranking_2023Mar.html
  * remark_ranking_20230401.csv
  * remark_ranking_2023Mar.csv

csvは、excelで直接開けます
もしくは、google スプレッドシートでimport可能です

