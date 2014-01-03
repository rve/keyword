import os
import csv
import re
import math
from gensim import corpora, models, similarities

if __name__ == '__main__':
    label_corpus = './data/label_corpus.csv'
    TEST=1
    dictionary = corpora.Dictionary(line.split() for line in
            open(label_corpus))
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if
            docfreq == 1]
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()


    r1 = open('./data/stest.csv')
    reader = csv.reader(r1)
    corpus = list()
    for row in reader:
        text = (row[1] + ' ' + row[2]).split()
        corpus.append(dictionary.doc2bow(text))
    print(corpus[:2])
    corpora.MmCorpus.serialize('./data/corpus.mm', corpus)
    print(dictionary)
    new_doc = 'javascript file upload'
    new_vec = dictionary.doc2bow(new_doc.lower().split())
    print(new_vec)
