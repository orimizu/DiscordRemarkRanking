set pythonutf8=1
chcp 65001

del tmp\*.csv
del tmp\*.html

rem    LOG_FILENAME は、ログのファイル名です。ファイル名は、Discordのログダウンローダがサーバ・スレッドごとに自動的に命名していますので、その名前を設定してください

set LOG_FILENAME=図月つくる2022誕生日記念LIVEサーバー - Text Channels - 雑談コーナー [1015156495366762533].json

rem    CHANNEL_NAME は、絵文字ランキングのタイトルに表示される、Discordサーバのチャネル名を指定します

set CHANNEL_NAME=図月つくるサーバー 雑談コーナー

rem    LOG_SUB_DIR は、ログ用のフォルダ名です。基本、ダウンロード日を使っています。以下のjsonファイルが存在する値に設定してください
rem    ..\log\%LOG_SUB_DIR%\%LOG_FILENAME%

set LOG_SUB_DIR=20230410

rem    2023年3月の月間集計、サーバ開始から2023年3月末までの集計をする場合
rem    B_YEAR=2023  B_MONTH=03 となります。

set B_YEAR=2023
set B_MONTH=3

rem    B_M_ENG には、B_MONTHの英語表記を入れます Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
rem    コマンドプロンプトでは、配列が使えないようなので、手動解決にぶん投げています

set B_M_ENG=Mar

rem    ここから下は、計算で自動的に決定しています

if exist "..\log\%LOG_SUB_DIR%\%LOG_FILENAME%" (
    echo "ログファイルが見つかりました"
) else (
    echo "ログファイル ..\log\%LOG_SUB_DIR%\%LOG_FILENAME% が見つかりません"
    echo "処理を終了します"
    exit /b
)


if exist "result\%LOG_SUB_DIR%" (
    del result\%LOG_SUB_DIR%\*.csv
    del result\%LOG_SUB_DIR%\*.json
    del result\%LOG_SUB_DIR%\*.html
) else (
    mkdir result\%LOG_SUB_DIR%
)

set /a A_MONTH=%B_MONTH%+1
if %A_MONTH%==13 (
    set A_MONTH=1
    set /a A_YEAR=%B_YEAR%+1
) else (
    set A_YEAR=%B_YEAR%
)

if %A_MONTH% LSS 10 (
    set Z_A_MONTH=0%A_MONTH%
) else (
    set Z_A_MONTH=%A_MONTH%
)
if %B_MONTH% LSS 10 (
    set Z_B_MONTH=0%B_MONTH%
) else (
    set Z_B_MONTH=%B_MONTH%
)

set A_YM=%A_YEAR%-%Z_A_MONTH%
set B_YM=%B_YEAR%-%Z_B_MONTH%
set B_YM_ENG=%B_YEAR%%B_M_ENG%


python discord_log_analysis.py %LOG_SUB_DIR% %A_YM% %B_YM% "%LOG_FILENAME%"
python reaction_image_csv2html.py 月間 %B_YEAR%年%B_MONTH%月版 "%CHANNEL_NAME%" > result\%LOG_SUB_DIR%\reaction_emoji_ranking_%B_YM_ENG%.html
copy /B UTF-8_BOM.txt result\%LOG_SUB_DIR%\remark_ranking_%B_YM_ENG%.csv
python sort_remark_ranking.py %B_YEAR%年%B_MONTH%月_月間 >> result\%LOG_SUB_DIR%\remark_ranking_%B_YM_ENG%.csv

python discord_log_analysis.py %LOG_SUB_DIR% %A_YM% TOTAL "%LOG_FILENAME%"
python reaction_image_csv2html.py 累計 %A_YEAR%/%A_MONTH%/1版 "%CHANNEL_NAME%" > result\%LOG_SUB_DIR%\reaction_emoji_ranking_%A_YEAR%%Z_A_MONTH%01.html
copy /B UTF-8_BOM.txt result\%LOG_SUB_DIR%\remark_ranking_2023%Z_A_MONTH%01.csv
python sort_remark_ranking.py %A_YEAR%/%A_MONTH%/1_累計 >> result\%LOG_SUB_DIR%\remark_ranking_%A_YEAR%%Z_A_MONTH%01.csv
