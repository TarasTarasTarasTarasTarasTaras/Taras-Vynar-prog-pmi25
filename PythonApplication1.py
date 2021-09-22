import random

def input_array(n, m, matrixA):
    print("Input the matrix of size " + str(n) + "x" + str(m))
    for i in range(n):
        for j in range(m):
            matrixA[i][j] = int(input())

def input_random_from_A_to_B(n, m, matrixA):
    A = int(input(" Input A: "))
    B = int(input(" Input B: "))
    for i in range(n):
        for j in range(m):
            matrixA[i][j] = random.randint(A,B)

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
        int_menu = int(input("  Enter '1' if you want to fill in the matrix A yourself\n" + 
                             "  Enter '2' if you want to fill the matrix A with random numbers from A to B\n" +
                             "  Enter '3' if you want to exit\n"))
        if int_menu == 3: break
        elif (int_menu < 1 or int_menu > 3):
            print("Please try again")
            continue
        else:
            n = int(input("Input N: "))
            m = int(input("Input M: "))
            if (n <= 1 or m <= 1):
                print("N and M must be '>' 1")
                continue

            matrixA = [[0 for i in range(m)] for j in range(n)]
            if int_menu == 1: input_array(n, m, matrixA)
            else: input_random_from_A_to_B(n, m, matrixA)

        matrixB = [[0 for i in range(m)] for j in range(n)]
        build_matrixB(matrixA, matrixB)

        print("\n\n  MATRIX A")
        print_array(n,m,matrixA)

        print("\n  RESULT: MATRIX B")
        print_array(n,m,matrixB)

        string = input("\n If you want to finish enter 'exit': ")
        if(string == "exit"): break

    except ValueError:
        print(" ERROR: Variable must be INT\n")
        continue
