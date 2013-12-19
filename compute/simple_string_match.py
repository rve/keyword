#coding: utf-8
import csv
import os
import re
import math
import shelve

if __name__ == '__main__':
    rfile = open("./data/o2test.csv")
    reader = csv.reader(rfile)
    #reader.next() # title
    new_t = 'data/simple.csv'
    writer = open(new_t, "wb")
    rlabel = open("./data/label.csv")
    flabel = csv.reader(rlabel)
    labels = list()
    for row in flabel:
        labels.append(row[0])
    cutvalue = 600 
    labels =labels[:cutvalue]
   
    nrows = 0
    docs_file = './data/docs.db'
    f_file = './data/f.db'
    size_d_file = './data/size_d.db'
    docs=dict()
    f=dict()
    size_d = dict()
    #docs = shelve.open(docs_file)
    #f=shelve.open(f_file)
    #size_d = shelve.open(size_d_file)
    for row in reader:
        docid = row[0]
        text = row[1]+' ' + row[2]
        words = text.split()
        ans = list()
        cnt = 0
        for label in labels:
            label = label.lower()
            if cnt >= 5:
                break
            if label in words:
                cnt += 1
                ans.append(label)

        writer.write('%s,"%s"\n' % (docid,' '.join(ans)))
        
        if nrows % 10000 == 0:
            print ('iter1: ',nrows)
        nrows += 1
        
#       top5 = tf_idf[:5]
#       ans = [item[1] for item in top5]
#       prio = [item[0] for item in top5]
        
        #writer.write('"%d","%s","%s"\n' % (docid,' '.join(ans), repr(prio)))

    writer.close()
    rfile.close()
    rlabel.close()

    




















