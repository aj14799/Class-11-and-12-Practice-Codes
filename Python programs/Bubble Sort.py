#Bubble Sort
def swapElements(aList):
    i = 0
    while(i < len(aList)-1):
        if (aList[i]>aList[i+1]):
            temp = aList[i]
            aList[i] = aList[i+1]
            aList[i+1] = temp
        i = i+1
        print ("List after pass", (i), ":", aList)

def bubbleSort(aList):
    for num in range(len(aList)-1):
        print( "----Itertion", num, "---")
        swapElements(aList)


#-----MAIN-----
aList = [15, 6, 13, 22, 3, 52, 2]
print("Original list is : ", aList)
bubbleSort(aList)
print("List after sorting : ", aList)
