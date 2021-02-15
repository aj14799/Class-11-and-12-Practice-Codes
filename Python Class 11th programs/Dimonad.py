def run():
    k = int(input("Enter range1:"))
    p = int(input("Enter range2:")) 
    if k>1 and p>1 and k==p:
        for i in range(k):
            print (" "*k,"# "*(i+1))
            k-=1
        for i in range(p):
            print (" "*(i+2),"# "*(p-1))
            p-=1
    else:
        print("Cann't form dimond")

run()            
            
            


















