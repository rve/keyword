from bs4 import BeautifulSoup
import csv

if __name__ == '__main__':
    ifile = open("data/Test.csv","rb")
    reader = csv.reader(ifile)
    d = ''
    reader.next()
    for row in reader:
        d += row[1]
        d += row[2]
    soup = BeautifulSoup(d)
    print soup.get_text()
    

    
