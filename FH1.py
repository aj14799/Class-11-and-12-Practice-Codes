#Consecutive Space to Single Space

import os

f = open('file1.txt','r')
f2 = open('tmp.txt', 'w')
data = f.read()
new = data[0]
for i in range(1, len(data)):
    ch = data[i]
    if new[-1] == ' ' and ch == ' ':
        continue
    new+= '#'
    break

f2.write(new)
f.close()
f2.close()
os.remove('file1.txt')
os.rename('tmp.txt', 'file1.txt')
