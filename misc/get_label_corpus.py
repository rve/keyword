#coding: utf-8
import csv
import os
import re
import sys

if __name__ == '__main__':
    TEST = 1
    train = './data/o1train.csv'
    if TEST == 1:
        train = './data/strain.csv'
    r1 = open(train)
    reader = csv.reader(r1)
    w1 = open('./data/label_corpus.csv', 'wb')
    for row in reader:
        w1.write('%s\n' % row[3])
    r1.close()
    w1.close()
