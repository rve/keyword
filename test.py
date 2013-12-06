import shelve

s = shelve.open('test.db')
s['key1'] = "123"
s.close()

s = shelve.open('test.db')
print 'key1: ',s['key1']
s.close()
