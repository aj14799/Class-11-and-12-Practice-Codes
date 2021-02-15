#To Count 'The' and 'To' in file

f = open('file2.txt','r')
d = f.read()
rec = d.split()
count_to = 0
count_the = 0
for word in rec:
    if word =='to' or word == 'To' or word =='TO':
        count_to+=1
    elif word == 'the'or word == 'The' or word =='THE':
        count_the+=1

print ("No. of To's=", count_to, "and No. of The's", count_the)
