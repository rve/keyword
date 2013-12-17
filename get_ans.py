#coding: utf-8
import csv
import os
import re
import math
import shelve

if __name__ == '__main__':
    rfile = open("./data/Test.csv")
    r1 = csv.reader(rfile)
    #reader.next() # title
    f1_a = 'data/f1_a.csv'
    w1 = open(f1_a, "wb")
    f1_b = 'data/f1_b.csv'
    w2 = open(f1_b, "wb")
    rlabel = open("./data/tfidf_ans.csv")
    r2 = csv.reader(rlabel)
    for row in r1:
        w1.write('%s\n'%row[3])
    for row in r2:
        #w2.write('%s\n'%row[1])
        w2.write('c# java php javascript android\n')
    w2.close()
    w1.close()
    rfile.close()
    rlabel.close()

    
