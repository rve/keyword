#coding: utf-8

import csv
import nltk
import sys
import re
#from nltk.corpus import stopwords as sw
#from nltk.stem.lancaster import LancasterStemmer
def stem(word):
    return word

def poss_train(train_file,train_write,sw_file):
    """
    
    Arguments:
    - `train_file`:
    """
    a = 0
    f = open(train_file)
    reader = csv.reader(f)

    t = open(train_write,"w")

    sw = open(sw_file)
    sw = sw.readlines()
    sw = [word.strip() for word in sw]
    
    #stopwords = sw  # use nltk stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    print "停顿词表长度",len(stopwords)
    stopwords = set(stopwords)

    g = lambda x : x not in stopwords
    
    for row in reader:
        if a%100000 == 0:
            print a    
        a += 1
        title = row[1].lower()
        #clean html
        body = nltk.clean_html(row[2].lower())
        
        #word tokenize
        pattern = r"([a-z])\w+"
        body = nltk.regexp_tokenize(body, pattern)
        title = nltk.regexp_tokenize(title, pattern)
        
        #remove stopwords
        body = filter(g,body)
        title = filter(g,title)

        #light stem
        #st = LancasterStemmer()
        title = set([stem(word) for word in title])
        body = set(body)
        body = set([stem(word) for word in body])

        # list to string
        body = ' '.join(body)
        title = ' '.join(title)
        t.write('"%s","%s","%s","%s"\n'%(row[0], title,body,row[3]))

def poss_test(test_file,test_write,sw_file):
    """
    
    Arguments:
    - `train_file`:
    """
    a = 0
    f = open(test_file)
    reader = csv.reader(f)

    t = open(test_write,"w")

    sw = open(sw_file)
    sw = sw.readlines()
    sw = [word.strip() for word in sw]
    
    #stopwords = sw 
    stopwords = nltk.corpus.stopwords.words('english')
    print "停顿词表长度",len(stopwords)
    stopwords = set(stopwords)

    g = lambda x : x not in stopwords
    
    for row in reader:

        if a%10000 == 0:
            print a    
        a += 1
        #if a == 8:
        #    sys.exit(1)

        title = row[1].lower()
        #clean html
        body = nltk.clean_html(row[2].lower())
        
        #work tokenize
        pattern = r"([a-z])\w+"
        body = nltk.regexp_tokenize(body, pattern)
        title = nltk.regexp_tokenize(title, pattern)
        #remove stopwords
        body = filter(g,body)
        title = filter(g,title)

        #light stem
        title = set([stem(word) for word in title])
        body = set(body)
        body = set([stem(word) for word in body])


        body = ' '.join(body)
        title = ' '.join(title)
        t.write('"%s","%s","%s"\n'%(row[0],title,body))

def usage():
    """
    """
    print '''
    这个是用nltk 的tokinize 做的预处理，请输入，训练文件+测试文件：
             python pre_nltk.py ../data/Train.csv ../data/Test.csv ../data/train.csv ../data/test.csv ../data/stopwords.txt
    '''
    
    


if __name__ == '__main__':
    if len(sys.argv) == 6:
        usage()
        train_file = sys.argv[1]
        train_write = sys.argv[3]
        test_file = sys.argv[2]
        test_write = sys.argv[4]
        sw_file = sys.argv[5]
    else:
        train_file = './data/o1train.csv'
        train_write = './data/nltk_without_stem.csv'
        test_file = './data/Test.csv'
        test_write = './data/nltk_o.csv'
        sw_file = './data/sw.txt'
    
    print "训练文件",train_file
    print "测试文件",test_file
    print "写入训练文件",train_write
    print "写入测试文件",test_write
    print "停顿词表文件",sw_file

    poss_train(train_file,train_write,sw_file)
    #poss_test(test_file,test_write,sw_file)
