def desending_odd_series():
    n=int(input("Enter Range (stating pt. of series:"))
    a=n%2
    if a==0:
        print(n,"is even number so starting pt. of series will",n-1)
        for i in range(n-1,0,-2):
            print(i)
        print("Desending Order of Odd Numbers")    
    else:
        for i in range(n,0,-2):
            print(i)
        print("Desending Order of Odd Numbers")    
desending_odd_series()
