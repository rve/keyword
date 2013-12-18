#!/bin/python
import csv
import os
import sys


real_file_name = './data/simple.csv'
f1 = open(real_file_name, 'r')
rc = csv.reader(f1)
real_file = f1.readlines()
print len(real_file)
print real_file[0]
print real_file[1]
print real_file[len(real_file)-1]
maxl = 8047532- 6034195
print maxl, len(real_file)-1
