#Selection Sort
def selection_sort(list1):
    for curPos in range(len(list1)):
        minPos = curPos # Starting with the current position

        for scanPos in range(curPos+1, len(list1)):
            if list1[scanPos] > list1[minPos]:
                minPos = scanPos

            # Swaping
            temp = list1[minPos]
            list1[minPos] = list1[scanPos]
            list1[scanPos] = temp

#----MAIN-----

list1 = [15, 6, 13, 22, 3, 52, 2]
print "Original list is : ", list1
selection_sort(list1)
print "List after sorting :", list1
            
                
