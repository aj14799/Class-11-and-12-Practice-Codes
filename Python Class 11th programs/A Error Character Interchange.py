a=input("Enter no.")
s=""
while True:
    if a=='q':
        quit()
    else:
        for i in range(0, len(a)):
            x=a[i]
            z=ord[x]
            if z>=65 and z<90:
                z-=32
            elif z>=99 and z<=122:
                z-=32
                x=ch[z]
                s+=x
print(s)

