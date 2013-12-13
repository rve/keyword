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

otest: original test

Todo:
1. also remove <code>(.?*)</code> multiline using regex
2. title priority in tf-idf
