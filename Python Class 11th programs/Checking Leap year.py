def Year():
    while True:
        print("Enter 0 or any -ve number key for exit or continue by Entering the Value")
        n = int(input("Enter Year:"))
        a = n%4
        if n>0:
            if a==0:
                print(n,"Year is Leap")
            else:
                print(n,"Year is not Leap")
        else:
            exit()
Year()
