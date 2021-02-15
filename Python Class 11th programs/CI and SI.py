def com():
    a=int(input("Enter '1' for Compound Interest or '2' for Simple Interest"))
    if a==1:
        Amount=float(input('Enter Amount'))
        Rate=float(input('Enter Rate'))
        Time=float(input('Enter Time'))
        SI=1+Rate/100
        Compound_Intrest=Amount*(SI**Time)
        print ('YOur Compound Intrest is', Compound_Intrest)
        Intrest=Compound_Intrest-Amount
        print('You get the intrest of',Intrest)
    elif a==2:
        Amount=float(input('Enter Amount'))
        Rate=float(input('Enter Rate'))
        Time=float(input('Enter Time'))
        Simple_Intrest = (Amount*Rate*Time)/100
        print('You got ur Simple_Intrest',Simple_Intrest)
    else:
        print("Quit")



