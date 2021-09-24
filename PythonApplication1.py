import random

def input_array(matrixA):
    print("\n Input the matrix of size " + str(len(matrixA)) + "x" + str(len(matrixA[0])))
    while True:
        try:
            for i in range(len(matrixA)):
                for j in range(len(matrixA[i])):
                    matrixA[i][j] = int(input("Matrix A["+str(i+1)+"]["+str(j+1)+"] = "))
            break
        except:
            print(" ERROR: Value must be INT")
            continue
                    

def input_random_from_A_to_B(matrixA, A, B):
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            matrixA[i][j] = random.randint(A,B)


def print_array(matrixA):
    for i in range(len(matrixA)):
        string = ""
        for j in range(len(matrixA[i])):
            string += str(matrixA[i][j]) +  " "
        print(string)
    print('\n')
        

def build_matrixB(matrixA, matrixB):
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            for k in range(i, len(matrixA)):
                matrixB[i][j] += matrixA[k][j]


def menu():
    while True:
        str_menu = input("  Enter 'random' if you want to fill the matrix A with random numbers from A to B\n" +
                         "  Enter 'fill' if you want to fill in the matrix A yourself\n" + 
                         "  Enter 'exit' if you want to exit\n")

        if str_menu == "exit": 
            break
        elif str_menu != "fill" and str_menu != "random":
            print("\nPlease try again")
            continue
        else:
            n = m = 0
            while (n <= 0 or m <= 0):
                print("\nN and M must be '>' 0")
                try:
                    n = int(input("Input N: "))
                    m = int(input("Input M: "))
                except: 
                    print(" ERROR: N and M must be INT")
                    continue

            matrixA = [[0 for i in range(m)] for j in range(n)]
            if str_menu == "fill": 
                input_array(matrixA)
            else:
                while True:
                    try:
                        A = int(input(" Input A: "))
                        B = int(input(" Input B: "))
                        break
                    except: 
                        print("ERROR: A and B must be INT")
                        continue
                if A > B: 
                    A=A+B; 
                    B=A-B; 
                    A=A-B;
                input_random_from_A_to_B(matrixA, A, B)

        matrixB = [[0 for i in range(m)] for j in range(n)]
        build_matrixB(matrixA, matrixB)

        print("\n\n  MATRIX A")
        print_array(matrixA)

        print("  RESULT: MATRIX B")
        print_array(matrixB)


menu()
