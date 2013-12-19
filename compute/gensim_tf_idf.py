import os
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
    print(dictionary)

