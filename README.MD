For test.csv
1. remove code
2. nltk preprocess
3. tf-idf 

For train.csv
1. remove code and same (n: 6m -> 4m, v: 7G -> 2.8G)
2. nltk preprocess (v: 2.8G -> 1.2G)

For data:
otrain: original train 
o1train: remove code and same (2.8G)
o2train: light stem (1.2G)
o3train: nltk stem (1.1G)
o4train: nltk without stem
o5train: nltk without stem, remove rare words
o6train: not remove same, only remove code (new startpoint)
o7train: remove code and same , new nltk for gensim

otest: original test
o1test: remove code
o2test: remove code, nltk without stem
o4test: +new nltk

strain: 30000data, remove code
s2train: +nltk

stest: 10000data ,remove code
s2test: +nltk
s3test: +tf-idf resorted

F1:
==== 10000 data ====
top 2000 label math with freq prio : 0.243 (using new label from 10000data)
tf-idf with labels : 0.093
tf-idf with text+labels: 0.06  233333
tf-idf with all labels: 0.086  233333
tf-idf with own tags: 0.27

=== all data ====
top 600: 0.679
top 2000: 0.673
