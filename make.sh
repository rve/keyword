#!/bin/bash


#echo "将出现频率少于20次的词全部加入停顿词表中"
#python2 remove_rare.py ../data/train.csv ../data/test.csv ../data/new_stopwords.txt

#echo "合并两个停顿词表"
#python2 hebing.py

#echo "重新处理文件，分成train和test"
#python2 ./preprocess/pre_nltk.py ./data/Train.csv ./data/Test.csv ./data/train.csv ./data/test.csv ./data/stopwords.txt

#echo "记录test的词表，移除test中未出现而train中出现的词"
#python2 remove_unseen.py ../data/train.csv ../data/test.csv ../data/test_vocab.txt ../data/new_train.csv

#echo "给关键词编码"
#python2 coding.py ../data/keyword_freq.txt ../data/test_vocab.txt ../data/coding_keyword.txt ../data/coding_vocab.txt

#echo "update code frequence"
#python2 count_freq.py data/Train.csv data/stopwords.txt data/cf.txt

#echo "get label (column 0)"
#python2 ./preprocess/get_label.py

#echo "run learning/just_couting.py"
#python2 ./learning/just_counting.py ./data/test.csv ./data/cf.txt
#echo "print head -n 3 result"
#head -n 15 ./data/result.csv
echo "完成"

