#!/user/bin/env python
# -*- coding: utf-8 -*-

# "tmp/01.txt", ファイル内の文章を形態素解析して、マルコフ連鎖で
# "tmp/01.txt", ファイル内の文章 を元に文章を自動作成するプログラム

import re
import MeCab
import random

def Mecab_file():
    #f = open("test.txt","rb")
    f = open("tmp/01.txt","rb")
    data = f.read()
    f.close()

    mt = MeCab.Tagger("-Owakati -d /usr/lib64/mecab/dic/mecab-ipadic-neologd")

    wordlist = mt.parse(data)
    wordlist = wordlist.rstrip(" \n").split(" ")

    markov = {}
    w = ""
    for x in wordlist:
        if w:
            if markov.has_key(w):
                new_list = markov[w]
            else:
                new_list =[]

            new_list.append(x)
            markov[w] = new_list
        w = x
        #print x

    #choice_words = wordlist[1]
    choice_words = random.choice(wordlist)
    sentence = ""
    count = 0
    #while count < 90:
    leng = len(wordlist)
    if leng > 30:
        leng = 30
    while count < leng:
        if markov.has_key(choice_words) != True:
            choice_words = wordlist[0]     
        
        sentence += choice_words
        choice_words = random.choice(markov[choice_words])
        count += 1

        sentence = sentence.split(" ", 1)[0]
        p = re.compile("[!-/:-@[-`{-~]")
        sus = p.sub("", sentence)

        random_words_list = [u"。", u"です。", u"だ。"]
        last_word = random.choice(random_words_list)

    print re.sub(re.compile("[!-~]"),"",sus), last_word

if __name__ == "__main__":
    Mecab_file()
