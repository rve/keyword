#coding: utf-8
import csv
import os
import re
import math
import shelve

if __name__ == '__main__':
    rfile = open("./data/Test.csv")
    reader = csv.reader(rfile)
    #reader.next() # title
    new_t = 'data/tfidf_ans.csv'
    writer = open(new_t, "wb")
    rlabel = open("./data/label.csv")
    flabel = csv.reader(rlabel)
    labels = list()
    for row in flabel:
        labels.append(row[0])
    cutvalue = 2000
    labels =labels[:2000]
   
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
        docid = (row[0])
        text = row[1]+' ' + row[2]
        words = text.split()
        size_d[docid]=len(words)
        f.setdefault(docid,dict())
        for word in words:
            f[docid].setdefault(word,0)
            if f[docid][word] == 0:
                docs.setdefault(word,0)
                docs[word]+=1
            f[docid][word] += 1
        
        if nrows % 10000 == 0:
            print ('iter1: ',nrows)
        nrows += 1
        
    computed = dict()
        #remove low freq tags
    thres = 10
    for k, v in docs.items():
        if v < thres:
            docs[k] = 0
            computed[k] = 1
        
    a = 0

    rfile.close()
    rfile = open("./data/Test.csv")
    reader = csv.reader(rfile)
    for row in reader:
        if a % 10000 == 0:
            print('iter2: ',a)
        a += 1

        text = row[1]+' '+ row[2]
        docid = (row[0])
        tf_idf = list()
        for word in text.split():
            computed.setdefault(word,0)
            if computed[word] == 0:
                computed[word] = 1
                tf = f[docid][word]/(size_d[docid]+0.0)
                idf = math.log((nrows+0.0)/docs[word])
                tf_idf.append((tf*idf, word))
        tf_idf.sort(reverse=True)
        tmp = tf_idf[:100]
        top100 = dict()
        for k,v in tmp:
            top100[v] = k
        counter = 0
        ans = list()
        prio = list()
        for key in labels:
            if counter < 5:
                if key in top100:
                    counter += 1
                    ans.append(key)
                    prio.append(top100[key])
        if counter == 0:
            for i in range(5):
                ans.append(str(i))

#       top5 = tf_idf[:5]
#       ans = [item[1] for item in top5]
#       prio = [item[0] for item in top5]
        
        #writer.write('"%d","%s","%s"\n' % (docid,' '.join(ans), repr(prio)))
        writer.write('"%s","%s"\n' % (docid,' '.join(ans)))
    writer.close()
    rfile.close()
    rlabel.close()

    
