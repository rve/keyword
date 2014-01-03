import os
import csv
import re
import math
from gensim import corpora, models, similarities

if __name__ == '__main__':
    label_corpus = './data/scorpus.csv'
    dictionary = corpora.Dictionary(line.split() for line in
            open(label_corpus))
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if
            docfreq == 1]
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()

    r1 = open('./data/o4test.csv')
    reader = csv.reader(r1)
    corpus = list()
    a =0
    for row in reader:
        a+=1
        if a % 10000 == 0:
            print('iter1 ' + str(a))
        text = (row[1] + ' ' + row[2]).split()
        corpus.append(dictionary.doc2bow(text))
    corpora.MmCorpus.serialize('./data/corpus.mm', corpus)
    r1.close()

    tfidf = models.TfidfModel(corpus)
    w1 = open('./data/tmp.csv','wb')
    a = 0
    for vec in corpus:
        a += 1
        if a % 10000 == 0:
            print('iter2 '+ str(a))
        tmp = tfidf[vec]
        ans = sorted(tmp, key=lambda x:x[1], reverse=True)
        ans = ans[:5]
        for kid, v in ans:
            if v > 0.20:
                w1.write('%s ' % (dictionary[kid]))
        w1.write('\n')
    w1.close()


