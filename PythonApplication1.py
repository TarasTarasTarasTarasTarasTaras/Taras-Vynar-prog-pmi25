class MyClassException(Exception): pass

def input_array(n, m, matrixA):
    print("Input the matrix of size " + str(n) + "x" + str(m))
    for i in range(n):
        for j in range(m):
            matrixA[i][j] = int(input())

def print_array(n, m, matrixA):
    for i in range(n):
        string = ""
        for j in range(m):
            string +=str(matrixA[i][j]) +  " " 
        print(string)
        

def build_matrixB(matrixA, matrixB):
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            for k in range(i, n):
                matrixB[i][j] += matrixA[k][j]

while True:
    try:
        n = int(input("Input N: "))
        m = int(input("Input M: "))

        if (n <= 1 or m <= 1): raise MyClassException

        matrixA = [[0 for i in range(m)] for j in range(n)]
        input_array(n,m,matrixA)

        matrixB = [[0 for i in range(m)] for j in range(n)]
        build_matrixB(matrixA, matrixB)

        print("\n\n")
        print_array(n,m,matrixA)

        print("\n\n")
        print_array(n,m,matrixB)

        string = input("\n\n If you want to finish enter 'exit': ")
        if(string == "exit"): break

    except ValueError:
        print(" ERROR: Variable should be INT\n")
        continue
    except MyClassException:
        print(" ERROR: N and M should be '>' 1\n")
        continue
