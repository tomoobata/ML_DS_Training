#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
    CSVファイルを読み込み、一列ごと空けて行く
"""

import csv

# 読み込みファイル
in_file = 't.csv'
fr = open(in_file, "r")
readcsv = csv.reader(fr)
data = [ v for v in readcsv ] # 読み込みCSVファイルデータをリストのリストで取得

col = len(data)       # 行
row = len(data[0])*2  # 列 # 変更後の列は (読み込みCSVファイルの列) x2のため"*2"

# 変更後の配列が入るオブジェクト
# 空の(col x row)配列を作成
cnv = []
for i in range(col):
   tmp = []
   for j in range(row):
       tmp.append('')
   cnv.append(tmp)

# すべて空列のcnvに2列ごとに読み込みCSVデータ列を入れる処理
for i in range(col):
    for j in range(row // 2):
        # 2 x jの列に jの列のdataデータを代入 
        cnv[i][2*j] = data[i][j]

# 書き込みファイル
fw = open('t-out.csv', 'w')
writer = csv.writer(fw, lineterminator='\n')
writer.writerows(cnv)
fw.close()

fr.close()