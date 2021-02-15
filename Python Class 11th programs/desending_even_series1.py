def desending_even_series():
    n=int(input("Enter Range stating pt. of series:"))
    a=n%2
    if a==0:
        for i in range(n,0,-2):
            print(i)
        print("Desending Order of Even Numbers")    
    else:
        print(n,"is odd number so starting pt. of series will",n-1)
        for i in range(n-1,0,-2):
            print(i)
        print("Desending Order of Even Numbers")    
desending_even_series()
