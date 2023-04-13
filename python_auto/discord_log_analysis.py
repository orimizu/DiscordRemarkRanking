#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import datetime
import time
import sys
import os

# Discordのログは、DiscordChatExporter でダウンロードすることを想定しています
# DiscordChatExporter自体は、GitHubで公開されており、以下のURLのReadme.mdのDownloadのセクションのリンク先でダウンロードできます
# https://github.com/Tyrrrz/DiscordChatExporter
#
# ドキュメントは以下を参照してください
# https://github.com/Tyrrrz/DiscordChatExporter/tree/master/.docs


if ( len(sys.argv) < 3):
    print('python %s <log file dir(sub dir of ../logl/)> <this month(yyyy-mm)> <last month(yyyy-mm)|TOTAL>' % my_file)
    sys.exit(0)

my_file = sys.argv[0]
log_dir = sys.argv[1]

json_path = "../log/" + log_dir + "/図月つくる2022誕生日記念LIVEサーバー - Text Channels - 雑談コーナー [1015156495366762533].json"
print("json_path: %s" % json_path)

if not os.path.isfile(json_path):
    print('python %s <log file dir(sub dir of ../logl/)> <this month(yyyy-mm)> <last month(yyyy-mm)|TOTAL>' % my_file)
    sys.exit(0)

if sys.argv[3] == 'TOTAL':
    time_start_filter = "2000-01-01T09:00:00.000+00:00"
else: 
    time_start_filter = sys.argv[3] + "-01T09:00:00.000+00:00"

time_end_filter = sys.argv[2] + "-01T08:59:59.999+00:00"

print("json_path: %s" % json_path)
print("time_start_filter: %s" % time_start_filter)
print("time_end_filter: %s" % time_end_filter)


# ここでは、../log/20230304 に json形式でダウンロードしています。この辺は適宜修正してください
with open(json_path, "r") as fin:
    j = json.load(fin)

messages = j.get("messages", [])
remarks = {}
number_of_characters = {}
nickname_dic = {}
reaction_stats = {}
reaction_stats_day = {}
reaction_stats_monday = {}

# ■■ 実行前に、このフィルターの値を修正してください ■■
# 以下は、サーバ開始時点から2023/3/1 00:00 時点までの累計の集計です
# 単月の集計をしたい場合は、time_start_filter を time_end_filter の１か月前の日付にしてください
# 9:00 区切りになっているのは、DiscordのlogがUTCで格納されているためです　JSTに変換するために9:00を足しています
# time_start_filter = "2000-02-01T09:00:00.000+00:00"
# time_end_filter = "2023-03-01T08:59:59.999+00:00"

for m in messages:
    timestamp = m["timestamp"]
    message_id = m["id"]
    author_id = m["author"]["id"]
    author_name = m["author"]["name"]
    author_nickname = m["author"]["nickname"]
    remark_counts = len(m["content"])
    remark = m["content"]
    reactions = m["reactions"]

    # デバッグ用
    # print("%s, %s, %s, %s, %s, [%d] %s" % (message_id, timestamp, author_id, m["author"]["name"], m["author"]["nickname"], remark_counts, remark))

    # タイムスタンプで期間を切り出す。time_start_filterからtime_end_filterの期間内だけ集計
    if timestamp > time_end_filter:
        continue
    if timestamp < time_start_filter:
        continue

    # timestamp を python の datetime型に変換します
    # discordのtimezoneは右記のフォーマットになってます 2022-09-06T12:34:05.946+00:00
    # これを datetime型のフォーマットに変換します
    dt = re.sub('T', ' ', timestamp)
    # 上記変換で、右記のフォーマットになります 2022-09-06 12:34:05.946+00:00
    # こうなる、と書いていますが、実際にはブレるところが１か所あります。
    # 小数点以下の箇所が、例えば小数点以下が3桁固定なら 12:11:33.010+00:00 と表示されます
    # データの場合、実際には、12:11:33.01+00:00 と最後の0が抜けて表示されます。
    # そして、非常に面倒なことに小数点以下が丁度0の場合、.自体が表示されません
    # つまり、2022-09-06 12:34:05.000+00:00 を期待しているところでは、
    # 2022-09-06 12:34:05+00:00 と小数点以下の表示がまるっと落ちます
    # これを解消するために、まずは、dt が . を含んでいるか判定します
    # 含んでいなかったら、強制的に '000' を小数点以下の数字とします
    if '.' in dt:
        # .を含んでいる場合、この秒の小数点以下を取得します
        subsec = re.sub('^.*\.', '', dt)     # 前半 先頭から . までを削除
        subsec = re.sub('\+.*$', '', subsec) # 後半 +から先を削除
        # そして、これを後ろ0詰めの3桁にします
        subsec = (subsec + '000')[0:3]
    else:
        #こちらが、. を含まない場合 subsecを強制で '000'にします
        subsec = '000'
    # 小数点以下を削除します
    dt = re.sub('\.\d*\+', '+', dt)
    # そして、+の前に、subsecを挿入します
    dt = re.sub('\+', '.'+subsec+'+', dt)
    # そして、datetime.strptime()で読み取れる形式に変換します
    # discordではミリ秒で時間を持っていますが、python標準ではマイクロ秒で時間を持つため
    # 後ろに0を３個追加する必要があります。
    # そして、タイムゾーン表記を00:00形式から0000形式に変換します
    # また、その時にフォーマットが分かりやすいよう + の前に空白を一つ挿入します
    dt = re.sub('\+00:00', '000 +0000', dt)

    # 上記変換で、右記のフォーマットになります 2022-09-06 12:34:05.946000 +0000
    # これを、datetime.strptime()でdatetime型に変換
    dt_stamp = datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S.%f %z')
    # print("dt_stamp: %s" % dt_stamp)
    # この段階では、dt_stampがUTC(世界標準時)ベースなので、日本と9:00ズレます
    # つまり、午前0時から午前9:00までの発言が前日の日付に集計されてしまいます
    # それを防ぐため、dt_stampをJST(日本標準時)に変換します
    jst = datetime.timezone(datetime.timedelta(hours=9))
    jst_stamp = dt_stamp.astimezone(tz=jst)
    jst_date_stamp = jst_stamp.strftime('%Y%m%d')
    jst_date = jst_stamp.date()

    # もう一つ。ここで、この日付の週頭の日付を算出します
    # この週頭の日付をキーにした辞書にデータを突っ込むことで、 週ごとの集計を実施します
    # （主にリアクション集計で使用します）
    # ここでは、date.weekday()/datetime.weekday()を使用します
    # date.weekday()/datetime.weekday()は、月曜日を0。日曜日6として整数が帰ってきます。
    # この数値を、dateから引いてあげると、月曜日の日付の datetimeやdateを計算できます。
    # 上で算出した、jst_stampは、timedateですので、そのままweekday()を呼べます
    weekday = jst_stamp.weekday()

    # datetime型/date型は、timedelta型との加減算が可能です。
    # date型1 = date型2 + timedelta型1 とか date型1 = date型2 - timedelta型1 のような演算が
    # 可能となっています。
    # timedelta型は、date型同士の引き算か、datetime.timedelta()で生成できます
    monday_jst_stamp = jst_stamp - datetime.timedelta(hours=weekday)
    monday_jst_date_stamp = monday_jst_stamp.strftime('%Y%m%d')
    monday_jst_date = monday_jst_stamp.date()

    # リアクション集計
    # リアクションは、以下のような感じで、reactions の valueに、辞書の配列として格納されています
    """
      "reactions": [
        {
          "emoji": {
            "id": "",
            "name": "\uD83D\uDD27",
            "isAnimated": false,
            "imageUrl": "https://twemoji.maxcdn.com/v/latest/svg/1f527.svg"
          },
          "count": 14
        },
        {
          "emoji": {
            "id": "",
            "name": "\uD83D\uDC49",
            "isAnimated": false,
            "imageUrl": "https://twemoji.maxcdn.com/v/latest/svg/1f449.svg"
          },
          "count": 1
        }
      ],
    """
    # そのため、集計のポリシーは、
    # reactionsの配列をforで回します
    # 辞書の key emoji を見て、あれば以下の処理し、なければemojiではないので処理を飛ばします
    # emojiをキーにして辞書を取得。その辞書の中から、key imageUrl と key count の値を取得
    # リアクション集計用辞書に、imageUrlをキーとして、countの値を足しこみます
    # ここで、nameを使用しないのは、カスタム絵文字の見分けがつかないためです
    # カスタム絵文字は、すべて "__" の値になってしまい見分けがつきません
    # どうやって見分けるかというと、idが埋め込まれるのでidで見分ければいいのですが、
    # わざわざフィールドを２つ取るくらいなら、１つ見るだけで良いimageUrlで集計した方が
    # よかろうという判断で、nameを使わずにimageUrlを使っています
    for r in reactions:
        # 辞書にアクセスする方法には、dict["key"] と dict.get("key", default_value) の２通りあります
        # 前者は、dict内に "key"がキーの値が格納されていない場合にエラーになります
        # そのため、データ構造上必ず含まれることが確信できる場合か、
        # エラー処理が面倒だし別に使うの自分だけだし取り合えずエラー出てもいいやと思う場合に使います
        # あとはバグを発見するために、フォーマットがおかしい場合に例外を上げたい時かな？
        # それ以外の場合では、後者の方法を推奨します
        emoji_dict = r.get("emoji", None)
        if emoji_dict:
            # 全体集計
            imageurl = emoji_dict["imageUrl"]
            count = r["count"]
            if reaction_stats.get(imageurl, None):
                reaction_stats[imageurl] = reaction_stats[imageurl] + count
            else:
                reaction_stats[imageurl] = count

            # 日毎集計(現状出力していません)
            if reaction_stats_day.get(imageurl, None):
                if reaction_stats_day[imageurl].get(jst_date, None):
                    reaction_stats_day[imageurl][jst_date] = reaction_stats_day[imageurl][jst_date] + count
                else:
                    reaction_stats_day[imageurl][jst_date] = count
            else:
                reaction_stats_day[imageurl] = {}
                reaction_stats_day[imageurl][jst_date] = count

            # 週毎集計(現状出力していません)
            if reaction_stats_monday.get(imageurl, None):
                if reaction_stats_monday[imageurl].get(monday_jst_date, None):
                    reaction_stats_monday[imageurl][monday_jst_date] = reaction_stats_monday[imageurl][monday_jst_date] + count
                else:
                    reaction_stats_monday[imageurl][monday_jst_date] = count
            else:
                reaction_stats_monday[imageurl] = {}
                reaction_stats_monday[imageurl][monday_jst_date] = count

    # ここから先は、発言数・発言文字数の集計処理です
    # 発言数と発言文字数をnicknameをキーとした辞書に加算していきます
    if remarks.get(author_id, "") == "":
        remarks[author_id] = 1
        number_of_characters[author_id] = remark_counts
        nickname_dic[author_id] = author_nickname
    else:
        remarks[author_id] = remarks[author_id] + 1
        number_of_characters[author_id] = number_of_characters[author_id] + remark_counts

# ここから出力処理です

# 発言数と発言文字数の辞書に入っている内容を出力しています
print("output ./tmp/remarks_ranking.csv ...")
with open("./tmp/remarks_ranking.csv", "w", encoding='UTF-8') as fout:
    for k in remarks:
        # print('"%s","%s","%d","%d"' % (k, nickname_dic[k], remarks[k], number_of_characters[k]))
        fout.write('"%s","%d","%d"\n' % (nickname_dic[k], remarks[k], number_of_characters[k]))

# リアクションのイメージランキングの辞書の内容を出力しています
print("output ./tmp/reaction_image_ranking.csv ...")
with open("./tmp/reaction_image_ranking.csv", "w", encoding='UTF-8') as fout:
    for img in reaction_stats:
        fout.write('"%d","%s"\n' % (reaction_stats[img], img))

print("End")
