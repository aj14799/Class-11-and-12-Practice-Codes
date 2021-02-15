# Meanu Driven Program to show all functions of stack like Push, Pop, Peek with Overflow and Underflow
def isEmpty( stk ):
    if stk == []:
        return True
    else:
        return False

def Push(stk, item):
    stk.append(item)
    top = len(stk)- 1

def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)- 1
        return item

def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk)- 1
        return stk[top]

def Display(stk):
    if isEmpty(stk):
        print ("Stack Empty")
    else:
        top = len(stk)- 1
        print (stk[top], "<-top")
        for a in range(top-1,-1,-1):
            print (stk[a])

#------MAIN--------
Stack = []
top = None

while True:
    print ('''STACK OPERATIONS
1. Push
2. Pop
3. Peek
4. Display Stack
5.to exit''')
    ch = input("Enter your Choice(1-5)")
    if ch == '1':
        item = int(input('Enter Item:'))
        Push(Stack, item)
    elif ch == '2':
        item = Pop(Stack)
        if item =="Underflow":
            print("Underflow! Stack is Empty!!")
        else:
            print ("Popped item is", item)
    elif ch == '3':
        item = Peek(Stack)
        if item == "Underflow":
            print("Underflow! Stack is Empty!!")
        else:
            print ("Top most iten is", item)
    elif ch == '4':
        Display(Stack)
    elif ch == '5':
        break
    else:
        print ('Invalid Choices')
        
        
        
    
