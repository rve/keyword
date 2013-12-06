#coding: utf-8
'''
抽取训练数据400条，用来实验预处理等的效果
'''

import csv

if __name__ == '__main__':
    ifile = open("data/otest.csv","rb")
    reader = csv.reader(ifile)

    a = 0
    sample_size = 3000

    train = []

    i = 0
    for row in reader :
        train.append(row)
        i += 1
        if i > sample_size:
            break

    ifile.close()

    #train = [['"%s"' % w for w in word] for word in train]

    ofile = open("data/Test.csv", "wb")
    writer = csv.writer(ofile,quotechar='"',quoting=csv.QUOTE_ALL)
    writer.writerows(train)
    ofile.close()
    
