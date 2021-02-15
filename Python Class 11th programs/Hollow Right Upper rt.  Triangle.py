def tri():
    m = int(input("Enter Range1:"))
    n = m
    for i in range(m):
        for j in range(n):
            print('*' if i in [j, m-1] or j == 0 else ' ', end='')
        print()
tri()
