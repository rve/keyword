#coding: utf-8

import csv
import os
import re

if __name__ == '__main__':
    f = open("./data/otrain.csv")
    reader = csv.reader(f)
    reader.next() # title
    new_t = 'data/rm_code_t.csv'
    ofile = open(new_t, "wb")
    writer = csv.writer(ofile,quotechar='"',quoting=csv.QUOTE_ALL)

    a = 1

    for row in reader:
        body = row[2]
        row[2] = re.sub(re.compile('<pre>(.*?)</pre>',re.MULTILINE|re.DOTALL), '',row[2])
        row[2] = re.sub(r'\n\n','', row[2])
        writer.writerow(row)
        a += 1
        if a % 100000 == 0:
            print(a) 

    ofile.close()
    f.close()

    os.system('wc -l '+new_t)
    os.system('head -n 5 '+new_t)
