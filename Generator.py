# Fibonacci value using generator'
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
        
#-----MAIN-----
n = int(raw_input("Fibonacci value upto number:"))
for i in fibonacci(n):
    print i,
    
