while True:
    print("Enter 0 for Exit or any positive integer to continue")
    b = int(input("Enter Value for exit or for countinue:"))
    if b>0:
        n = float(input("Enter 1st Number:"))
        c = float(input("Enter 2nd Number:"))
        a = n-c
        if -0.001<=a<=0.001:
            print(n,"and", c,"Numbers are Close to each other")
        else:
            print(n,"and", c,"Numbers are Not Close to each other")
    else:
        quit()
 
