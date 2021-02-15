#linear Search
def Lsearch(AR, ITEM):
    i=0
    while i < len(AR) and AR[i] != ITEM:
        i+=1
    if i < len(AR):
        return i
    else:
        return False

#-----Main-----
N = int(raw_input("Enter desired linear-list size (max. 50)... "))
print "\nEnter elements for Linear List\n"
AR = [0]*N     # initialize List of size N with zeros
for i in range(N):
    AR[i] = int(raw_input(" Element"+str(i)+": "))
ITEM = int(raw_input("\nEnter Element to  be searched for... "))
index = Lsearch(AR, ITEM)
if index:
    print "\nElement found at index:", index,",Position: " ,(index+1)
else:
    print "\nSorry!! Given element could not be found.\n"


Lsearch(AR, ITEM)


        


    
