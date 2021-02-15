#Traversal a linear list
def traverse(AR):
    size = len(AR)

    for i in range(size):
        print AR[i],

#----MAIN----
size = int(raw_input("Enter the size of Linear List to be input: "))
AR = [None] * size
print "Enter elements for the Linear List:"
for i in range(size):
    AR[i] = int(raw_input("Element" + str(i) + ":"))
print "Traversing the list"
traverse(AR)
























