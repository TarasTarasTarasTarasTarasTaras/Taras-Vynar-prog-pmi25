def input_array(n, m, matrixA):
    for i in range(n):
        for j in range(m):
            matrixA[i][j] = int(input())

def print_array(n, m, matrixA):
    for i in range(n):
        string = ""
        for j in range(m):
            string +=str(matrixA[i][j]) +  " " 
        print(string)
        

def build_matrixB(martixA, matrixB):
    for i in range(len(matrixA)):
        for j in range(len(matrixB)):
            for k in range(i, m):
                matrixB[i][j] += matrixA[k][j]

n = int(input("Input N: "))
m = int(input("Input M: "))

matrixA = [[0 for i in range(n)] for j in range(m)]
input_array(n,m,matrixA)

matrixB = [[0 for i in range(n)] for j in range(m)]
build_matrixB(matrixA, matrixB)

print("\n\n")
print_array(n,m,matrixA)

print("\n\n")
print_array(n,m,matrixB)
