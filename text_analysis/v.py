# coding: UTF-8

import os # osモジュールのインポート
import codecs
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
c_vec = CountVectorizer(
    token_pattern=u'(?u)\\b\\w+\\b', 
    stop_words=[ 
        u"あ",u"い",u"う",u"え",u"お",u"か",u"き",u"く",u"け",u"こ",u"さ",u"し",u"す",u"せ",u"そ",u"た",u"ち",u"つ",u"て",u"と",u"な",u"に",u"ぬ",u"ね",u"の",u"ま",u"み",u"む",u"め",u"も",u"は",u"ひ",u"ふ",u"へ",u"ほ",u"ま",
u"み",u"む",u"め",u"も",u"や",u"ゆ",u"よ",u"ら",u"り",u"る",u"れ",u"ろ",u"わ",u"を",u"ん",
        u"その",u"から", u"ます", u"です", u"これ",u"たち", u"そこ", u"られ",u"ある",u"あり",u"よう", u"ない", u"なし",u"なら", u"れる", u"いる", u"する", u"こと", u"ため", u"それ", u"もの"])
#c_vec = CountVectorizer(min_df=1, stop_words=[u"なし"])
#c_vec = CountVectorizer()

f = codecs.open("NT2", 'r','utf_8')
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

#print type(data1)

c_vec.fit([data1])
c_terms = c_vec.get_feature_names()   # ベクトル変換後の各成分に対応する単語をベクトル表示
c_tran  = c_vec.transform([data1])  # 単語の数を数える
# print c_vec.get_stop_words()

# print "c_terms:", c_terms
#print "c_tran", c_tran.toarray()
#print c_tran
# ソート後の配列要素インデックスを得るには？ は numpy.argsort
# [::-1] を付けてソートを逆順(降順にしている)

#print c_tran.toarray()
#exit(1)

arg_ind = np.argsort(c_tran.toarray())[0][::-1]
#print arg_ind
# 単語を多い順に表示
#単語をソートしてコンマ","区切りで表示
for i in arg_ind:
    print c_vec.get_feature_names()[i].encode('utf-8'), ",",
print " "
for i in arg_ind:
    print c_tran.toarray()[0][i], ",",

