#!/usr/env python2
#coding: utf-8

import sys
import csv
import os
import shelve


if __name__ == '__main__':
    TEST = 0
    print(10*'=',__file__,' started',10*'=')
    if len(sys.argv) != 4:
        train_file = "./data/Train.csv"
        test_file = "./data/Test.csv"
        hresult_file = "./data/hresult.csv"
    else:
        train_file = sys.argv[1]
        test_file = sys.argv[2]
        hresult_file = sys.argv[3]
    tdict_file = './data/tdict.db'
    os.system('rm  -rf '+tdict_file) #delete it 
    tdict = shelve.open(tdict_file)
    f = open(train_file)
    train_reader = csv.reader(f)
    f2 = open(test_file)
    test_reader = csv.reader(f2)
    f3 = open(hresult_file,'w')
    real_file_name="./data/simple.csv"
    if TEST == 1:
        real_file_name = "./data/test_ans.csv"
    f4 = open(real_file_name, 'r')
    real_file = f4.readlines()

    
#    tdict = dict()
    train_reader.next()
    test_reader.next()
    a=0
    for row in train_reader:
        a += 1
        tdict[row[1]] = row[3]
        if a % 20000 == 0:
            print(a)
    f.close()
    f3.write('"Id","tags"\n')
    first_line_num = 6034195
    if TEST == 1:
        first_line_num = 0
    a=0
    for row in test_reader:
        a+=1
        if a % 20000 == 0:
            print(a)
        if row[1] in tdict:
            f3.write('%s,"%s"\n' % (row[0],tdict[row[1]]))
        else:
            line_num = int(row[0]) - first_line_num
            ans = real_file[line_num]
            #f3.write('%s,%s\n' % (row[0],'"c# java php javascript android"'))
            f3.write('%s\n' % ans)

    f2.close()
    f3.close()
    tdict.close()
    os.system('head -n 4 '+hresult_file)
    os.system('tail -n 4 '+hresult_file)
    os.system('wc -l '+hresult_file)
    print(10*'=',__file__,' ended',10*'=')

