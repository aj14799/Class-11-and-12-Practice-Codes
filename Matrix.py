#Matrix 1
def Matrix():
    m = int(input('number of rows, m = '))
    n = int(input('number of columns, n = '))
    matrix = []; columns = []
    # initialize the number of rows
    for i in range(0,m):
      matrix += [0]
    # initialize the number of columns
    for j in range (0,n):
      columns += [0]
    # initialize the matrix
    for i in range (0,m):
      matrix[i] = columns
    for i in range (0,m):
      for j in range (0,n):
        print ('entry in row: ',i+1, '\n',' column: ',j+1)
        matrix[i][j] = int(input())
    print ('Matrix1', matrix)

#Matrix 2
def Matrix2():

    a = int(input('number of rows, a = '))
    b = int(input('number of columns, b = '))
    matrix2 = []; columns2 = []
    # initialize the number of rows
    for k in range(0,a):
      matrix2 += [0]
    # initialize the number of columns
    for l in range (0,b):
      columns2 += [0]
    # initialize the matrix
    for k in range (0,a):
      matrix2[k3] = columns2
    for k in range (0,a):
      for l in range (0,b):
        print ('entry in row: ',k+1, '\n',' column: ',l+1)
        matrix2[k][l] = int(input())
    print ('Matrix12', matrix2)

Matrix()
Matrix2()