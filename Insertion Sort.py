#Insertion Sort

def insertionSort(AR):
    for i in range(1, len(AR)):
        v = AR[i]
        j = i

        while AR[j-1] > v and j>=1:
            AR[j] = AR[j-1]
            j -= 1
        #insert the value at its correct position
        AR[j] = v
        print "List after pass", (i), ":", list1

#-----MAIN-----
list1 = [15, 6, 13, 22, 3, 52, 2, 10]
print "Original list is :", list1
insertionSort(list1)
print "List after sorting :", list1
