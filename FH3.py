#To Convert Uppercase to Lowercase and Visa-Versa

import os

f = open('file3.txt','r')
f2 = open('tmp.txt','w')
data = f.read()
new =' '
for ch in data:
    if ch.isupper():
        ch = ch.lower()
    else:
        ch = ch.upper()
    new+=ch

f2.write(new)
f.close()
f2.close()
os.remove('file3.txt')
os.rename('tmp.txt', 'file3.txt')

         
