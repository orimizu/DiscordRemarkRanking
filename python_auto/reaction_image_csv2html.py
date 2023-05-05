#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import datetime
import time
import sys


month_or_total = sys.argv[1]
year_month = sys.argv[2]
channel_name = sys.argv[3]

print('<html>')
print('<head>')
print('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
print('<meta http-equiv="Content-Style-Type" content="text/css">')
print('<title>Zutsuki Tukuru Discord Server Log Analysis Emoji Ranking</title>')
print('<head>')
print('<body>')
print('<h1>Discord %s %s リアクション絵文字ランキング(%s)</h1>' % (channel_name, month_or_total, year_month))
#print('<h1>Discord 図月つくるサーバー 雑談コーナー %s リアクション絵文字ランキング(%s)</h1>' % (month_or_total, year_month))
#print('<h1>Discord 図月つくるサーバー 雑談コーナー 累計 リアクション絵文字ランキング(2023/3/1版)</h1>')
print('<table border="1" style="border-collapse: collapse">')
print('<tr><th>順位</th><th>使用回数</th><th>絵文字</th><th>URL</th></tr>')

#reaction_image_num_seq = []
#with open("./tmp/reaction_image_ranking.csv", "r", encoding='utf_8_sig') as fin:
#    r = fin.readline()
#    while r:
#        rs = r.strip().split(',')
#        num = int(rs[0].strip('"'))
#        reaction = rs[1].strip('"')
#        reaction_image_num_seq.append({"num": num, "reaction": reaction})
#        r = fin.readline()

with open("./tmp/reaction_image_ranking.json", "r", encoding='utf_8_sig') as fin:
    reaction_image_num_seq = json.load(fin)

sorted_reaction_image_num_seq = sorted(reaction_image_num_seq, key=lambda x: x["num"], reverse=True)

# 順位付け
reaction_image_ranking_seq = []
rank = 1
score = 0
i = 1
for dic in sorted_reaction_image_num_seq:
    if score > int(dic["num"]):
        rank = i
    score = int(dic["num"])
    reaction_image_ranking_seq.append({"rank": rank, "num": dic["num"], "reaction": dic["reaction"]})
    i = i + 1

for dic in reaction_image_ranking_seq:
    rank = dic["rank"]
    num = dic["num"]
    reaction = dic["reaction"]
    print('<tr><td>%s</td><td>%s</td><td><img src="%s" height="32"></td><td>%s</td></tr>' % (rank, num, reaction, reaction))

print('</table>')
print('</body>')
print('</html>')
