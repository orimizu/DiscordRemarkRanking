#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import datetime
import time
import sys
import csv

pre = sys.argv[1]

remark_ranking_seq = []
with open("./tmp/remarks_ranking.json", "r", encoding='utf_8_sig') as fin:
    remark_ranking_seq = json.load(fin)

sorted_remark_ranking_seq = sorted(remark_ranking_seq, key=lambda x: x["remarks"], reverse=True)
sorted_word_count_ranking_seq = sorted(remark_ranking_seq, key=lambda x: x["word_count"], reverse=True)

# 順位付け

print('"%s発言数ランキング",,,,,"%s発言文字数ランキング"' % (pre, pre))
print('"順位","ニックネーム","発言数","発言文字数",,,"順位","ニックネーム","発言数","発言文字数"')

rank1 = 0
rank2 = 0
r1_value = 0
r2_value = 0
l1 = len(sorted_remark_ranking_seq)
l2 = len(sorted_word_count_ranking_seq)
if l1 > l2:
    l_big = l1
else:
    l_big = l2

csv_writer = csv.writer(sys.stdout, lineterminator="\n")

for i in range(l_big):
    dic1 = sorted_remark_ranking_seq[i]
    dic2 = sorted_word_count_ranking_seq[i]
    nickname1 = dic1.get("nickname")
    nickname2 = dic2.get("nickname")
    remarks1 = dic1.get("remarks")
    remarks2 = dic2.get("remarks")
    word_count1 = dic1.get("word_count")
    word_count2 = dic2.get("word_count")
    if r1_value != remarks1:
        rank1 = i + 1
        r1_value = remarks1
    if r2_value != word_count2:
        r2_value = word_count2
        rank2 = i + 1
    if (i < l1) and (i < l2):
        csv_writer.writerow([rank1, nickname1, remarks1, word_count1, "", "", rank2, nickname2, remarks2, word_count2])
    if (i < l1) and (i >= l2):
        csv_writer.writerow([rank1, nickname1, remarks1, word_count1, "", "", "", "", "", ""])
    if (i >= l1) and (i < l2):
        csv_writer.writerow(["", "", "", "", "", "", rank2, nickname2, remarks2, word_count2])

