#!/bin/python
import csv
import os
import sys


def mean_f1_score(real_file_name, predict_file_name):
    f1 = open(real_file_name, 'r')
    rc = csv.reader(f1)
    real_file = f1.readlines()

    f2 = open(predict_file_name, 'r')
    pc = csv.reader(f2)
    
    predict_file = f2.readlines()

    if len(real_file) == len(predict_file):
        lines = len(real_file)
    else:
        print "real file lines unequal to predict file lines!!!"
        exit(1)

    score = 0.0
    for i in range(lines):
        real_labels = real_file[i].split()
        predict_labels = predict_file[i].split()
        true_positive_labels = list(set(real_labels) & set(predict_labels))

        true_positive = 1.0 *len(true_positive_labels)
        true = 1.0 * len(real_labels)
        positive = 1.0 * len(predict_labels)
        score += 2 * true_positive / (true + positive)

    score = score / lines
    
    f1.close()
    f2.close()
    return score

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print mean_f1_score('data/f1_a.csv','data/f1_b.csv')
    else:
        a = sys.argv[1]
        b = sys.argv[2]
        print mean_f1_score(a, b)
