#!/bin/bash
mv ./data/o2train.csv ./data/Train.csv
python  ./preprocess/pre_nltk.py
mv ./data/Train.csv ./data/o2train.csv

