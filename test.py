
d=dict()
d[1] =11
d[2] =22
d[3] =33
for k,v in d.items():
    if v < 20:
        del d[k]
print d

