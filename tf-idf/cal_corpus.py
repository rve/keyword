import os
import csv
import re
import math
from gensim import corpora, models, similarities

if __name__ == '__main__':
    label_corpus = './data/s2train.csv'
    TEST=1
    tmp = list()
    r1 = open(label_corpus)
    reader2 = csv.reader(r1)
    for row in reader2:
        text = (row[1] +  ' ' + row[2] + ' '+ row[3])
        tmp.append(text)
    dictionary = corpora.Dictionary(line.split() for line in
            tmp)
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if
            docfreq == 1]
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()
    r1.close()


    r1 = open('./data/s2test.csv')
    reader = csv.reader(r1)
    corpus = list()
    a = 1
    for row in reader:
        a += 1
        if a % 1000 == 0:
            print(a)
        text = (row[1] + ' ' + row[2]).split()
        corpus.append(dictionary.doc2bow(text))
    #corpora.MmCorpus.serialize('./data/corpus.mm', corpus)
    r1.close()

    w1 = open('./data/tmp.csv','wb')

    tfidf = models.TfidfModel(corpus)
    for vec in corpus:
        tmp = tfidf[vec]
        ans = sorted(tmp, key=lambda x:x[1], reverse=True)
        ans = ans[:5]
        for kid, v in ans:
            w1.write('%s ' % (dictionary[kid]))
        w1.write('\n')
    w1.close()


