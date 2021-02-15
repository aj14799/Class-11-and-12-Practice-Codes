m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [j, m-1] or j == 0 else ' ', end='')
    print()
