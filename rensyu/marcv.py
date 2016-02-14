#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import MeCab

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    #result = m.rstrip(" \n").split(" ")
    result = m.rstrip().split(" ")
    #print m
    #print result 
    return result

if __name__ == "__main__":
    filename = "test.txt"
    src = open(filename, "r").read()
    wordlist = wakati(src)

    # Create table of Markov Chain
    markov = {}
    w1 = ""
    w2 = ""
    #w3 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word
        #print w1, w2, w3
    
    #print markov
    print len(wordlist)

    # Generate Sentence
    count = 0
    sentence = ""
    w1, w2  = random.choice(markov.keys())
    while count < len(wordlist)/2:
        count += 1
        if markov.has_key((w1,w2)):
            tmp = random.choice(markov[(w1, w2)])
            sentence += tmp
            w1, w2 = w2, tmp
        if " " in sentence:
            sentence = sentence.split(" ", 1)[0]

    print sentence
