while True:
    print("Enter any Key instead of Positve Integral Value to exit or Enter value to countinue")
    n = int(input("Enter How many things Your Buying"))
    if 0<n<=10  :
        print("Total cost for your goods 120Rs")
    elif 10<n<99:
        print("Total cost for your goods 100Rs")
    elif n>100:
        print("Total cost for your goods 70Rs")
    else:
        exit()
    
