#coding: utf-8
import csv
import os
import re
import math
import shelve

if __name__ == '__main__':
    rfile = open("./data/s3test.csv")
    reader = csv.reader(rfile)
    new_t = 'data/tmp.csv'
    writer = open(new_t, "wb")
    rlabel = open("./data/slabel.csv")
    flabel = csv.reader(rlabel)
    labels = list()
    for row in flabel:
        labels.append(row[0])
    cutvalue = 600 
    labels =labels[:cutvalue]
   
    nrows = 0
    docs=dict()
    f=dict()
    size_d = dict()
    for row in reader:
        text = row[0]
        words = text.split()
        ans = list()
        cnt = 0
        dt = dict()
        for label in words:
            label = label.lower()
            if cnt >= 5:
                break
            dt.setdefault(label,0)
            if dt[label] == 0 and label in labels:
                dt[label] = 1
                cnt += 1
                ans.append(label)

        writer.write('%s\n' % (' '.join(ans)))
        
        if nrows % 10000 == 0:
            print ('iter1: ',nrows)
        nrows += 1

    writer.close()
    rfile.close()
    rlabel.close()
