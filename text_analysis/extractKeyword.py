#coding:utf-8
import MeCab
import codecs
import re

def extractKeyword(text):
    """textを形態素解析して、名詞 動詞 形容詞 のみのリストを返す"""
    #tagger = MeCab.Tagger('-Ochasen')
    tagger = MeCab.Tagger('-Ochasen -d /usr/lib64/mecab/dic/mecab-ipadic-neologd')

    encoded_text = text.encode('utf-8')
    node = tagger.parseToNode(encoded_text)
    #print type( node.feature.split(",")[0] )
    #print type(u"名詞")
    test_c =0
    pattern = r"(名詞|動詞|形容詞|副詞)"
    keywords = []
    while node:
        #if test_c < 300 and  node.surface == "主":
        #    print "node.feature:", node.feature, " node.surface:", node.surface
        #    test_c +=1
        #else:
        #    pass # exit(1)

        #tmp = node.feature.split(",")[0]
        tmp = node.feature
        if re.match(pattern , tmp):
        #if tmp == "名詞" or tmp =="動詞" or tmp == "形容詞":
        #if node.feature.split(",")[0] == u"名詞".encode('utf8') :
            keywords.append(node.surface)
        node = node.next
    return keywords

if __name__ == "__main__":
    f = codecs.open("out_nt2.txt", 'r','utf_8')
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()  

    #print data1  
      
#    lines1 = data1.split('\r\n')
#    for li in lines1: 
     #   keywords = extractKeyword(li)
    keywords = extractKeyword(data1)
    for w in keywords:
        print w,

