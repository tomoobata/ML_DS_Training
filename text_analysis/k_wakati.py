#coding:utf-8
import MeCab
import codecs

def wakati(text):
    """textを形態素解析して、名詞 動詞 形容詞 のみのリストを返す"""
    #tagger = MeCab.Tagger('-Owakati')
    #tagger = MeCab.Tagger('-Ochasen')
    tagger = MeCab.Tagger('-Owakati -d /usr/lib64/mecab/dic/mecab-ipadic-neologd')
    #tagger = MeCab.Tagger('-Ochasen -d /usr/lib64/mecab/dic/mecab-ipadic-neologd')

    encoded_text = text.encode('utf-8')
    node = tagger.parse(encoded_text)
    return node
    #print "node", node
    #exit(1)


if __name__ == "__main__":
    #f = codecs.open("fb_word_for_word2vec.txt", 'r','utf_8')
    f = codecs.open("../out_ot2.txt", 'r','utf_8')
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()  

    #print data1  
      
    writefile = file('OT2','w')
    lines1 = data1.split('\r\n')
    #lines1 = data1.split('\n')
    for i, li in enumerate(lines1): 
        w = wakati(li)
        #print "i:",i 
        writefile.write( w )
    writefile.close()
