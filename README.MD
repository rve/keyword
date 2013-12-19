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

F1:
==== 10000 data ====
top5: 0.83
top 200 label match with freq prio: 0.112 (label corrupted -- should use new nltk)
top 2000 ~ : 0.121
top 2000 label math with freq prio : 0.243 (using new label from 10000data)
top 400 ~ : 0.250
top 200 ~ : 0.243

=== all data ====
top 600: 0.679
top 2000: 0.673

Todo:
1. also remove <code>(.?*)</code> multiline using regex
2. title priority in tf-idf
