def tri():
    m = int(input("Enter Range1:"))
    n=m
    for i in range(m):
        for j in range(n):
            print('*' if j in [i, m-1] or i == 0 else ' ', end='')
        print()
tri()
