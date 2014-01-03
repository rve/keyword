import os
import csv
import re
import math
from gensim import corpora, models, similarities

if __name__ == '__main__':
    label_corpus = './data/label2f.csv'
    TEST=1
    dictionary = corpora.Dictionary([line.rstrip()] for line in
            open(label_corpus))
    dictionary.compactify()
    print(dictionary)

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
            if v > 0.28:
                #w1.write('%s:%s ' % (dictionary[kid], str(v)))
                w1.write('%s ' % (dictionary[kid]))
        w1.write('\n')
    w1.close()


