def Cost1():
    print("Total cost for your goods 120Rs")
def Cost_2():
    print("Total cost for your goods 100Rs")
def Cost__3():
    print("Total cost for your goods 70Rs")
while True:
    print("Enter 0 0r negative value to exit to exit or Enter value to countinue")
    n = int(input("Enter How many things Your Buying"))
    if 0<n<=10  :
        Cost1()
    elif 10<n<99:
        Cost_2()
    elif n>100:
        Cost__3()
    else:
        exit()
    
    
