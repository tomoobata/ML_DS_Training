# coding: UTF-8

import os # osモジュールのインポート
import codecs
import re

# os.listdir('パス')
# 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す

import MeCab

#tagger = MeCab.Tagger('-Owakati')
#tagger = MeCab.Tagger('-Ochasen -d /usr/lib64/mecab/dic/mecab-ipadic-neologd')
writefile = file('../out_ot2.txt','w')

f = codecs.open("../out_ot.txt", 'r','utf_8')
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

lines1 = data1.split('\r\n') # 改行で区切る(改行文字そのものは戻り値のデータに>は含まれない)


pattern = u"(第 \d{1,3}(章|篇)|■)"
repatter = re.compile(pattern)

for line in lines1:
#    pass
    #print "line:", line
    #print re.sub(repatter, "", line)
    writefile.write( re.sub(repatter, "", line).encode('utf-8')+'\r\n' ) 
#    writefile.write(tagger.parse( line.encode('utf8') ))
writefile.close()
