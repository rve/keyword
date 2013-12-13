#coding: utf-8

import csv
import os

if __name__ == '__main__':
    f = open("./data/Train.csv")
    reader = csv.reader(f)
    reader.next() # title
    rule = open("./data/label.csv")
    reader2 = csv.reader(rule)

    a = 1
    data = dict()

    for row in reader:
        for word in row[3].split():
            data.setdefault(word,0)
            data[word] += 1
            if a % 100000 == 0:
                print a
                a += 1
    tags = sorted(data.items(), key = lambda x : -x[1])
        
    ofile = open("data/label_train.csv", "wb")
    writer = csv.writer(ofile,quotechar='"',quoting=csv.QUOTE_ALL)
    writer.writerows(tags)
    ofile.close()
    
    os.system('wc -l data/label.csv')
    os.system('head -n 5 data/label.csv')
