#coding: utf-8
import csv
import os
import re
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('usage: self real_file_name predict_file_name')
        print ('output: data/f1_a.csv   data/f1_b.csv')
        print ('then use f1.py to calculate')
        #real_file = "./data/Train.csv"
        #predict_file = "./data/simple.csv"
        sys.exit(1)
    else:
        print ('='*10+ 'output: data/f1_a.csv   data/f1_b.csv' + '='*10)
        real_file = sys.argv[1]
        predict_file = sys.argv[2]
    rfile = open(real_file)
    r1 = csv.reader(rfile)
    #reader.next() # title
    f1_a = 'data/f1_a.csv'
    w1 = open(f1_a, "wb")
    f1_b = 'data/f1_b.csv'
    w2 = open(f1_b, "wb")
    rlabel = open(predict_file)
    r2 = csv.reader(rlabel)
    for row in r1:
        w1.write('%s\n'%row[3])
    for row in r2:
        w2.write('%s\n'%row[1])
       #w2.write('c# java php javascript android\n')
    w2.close()
    w1.close()
    rfile.close()
    rlabel.close()

    
