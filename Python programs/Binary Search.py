#Binary Search
def Bsearch(AR, ITEM):
    beg = 0
    last = len(AR)-1
    while(beg <= last):
        mid = (beg + last)/2
        if (ITEM == AR[mid]):
            return mid
        elif (ITEM > AR[mid]):
            beg = mid+1
        else:
            last = mid-1
    else:
        return False    # When item is not found

#----MAIN----
N = int(input("Enter desired linear-list size (max. 50)... "))
print( "\nEnter elements for Linear List\n, for binary search")
AR = [0]*N     # initialize List of size N with zeros
for i in range(N):
    AR[i] = int(input(" Element"+str(i)+": "))
ITEM = int(input("\nEnter Element to  be searched for... "))
index = Bsearch(AR, ITEM)
if index:
    print ("\nElement found at index:", index,",Position: " ,(index+1))
else:
    print ("\nSorry!! Given element could not be found.\n")

Bsearch(AR, ITEM)
