import random

def input_array(matrixA):
    print("\n Input the matrix of size " + str(len(matrixA)) + "x" + str(len(matrixA[0])))
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            matrixA[i][j] = enter_validated_number("Matrix A["+str(i+1)+"]["+str(j+1)+"] = ", "matrix element")
                    

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
        

def build_matrixB(matrixA):
    matrixB = [[0 for i in range(len(matrixA[0]))] for j in range(len(matrixA))]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            for k in range(i, len(matrixA)):
                matrixB[i][j] += matrixA[k][j]
    return matrixB


def enter_validated_number(string, key):
    try:
        number = int(input(string))
        if key == "size" and number < 1:
            raise SyntaxError
        return number
    except ValueError:
        raise ValueError("  ERROR: " + key + " must be INT\n")
    except SyntaxError:
        raise ValueError("  ERROR: size must be greater than 0\n")


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
            try:
                n = enter_validated_number("Enter rows: ", "size")
                m = enter_validated_number("Enter columns: ", "size")
                matrixA = [[0 for i in range(m)] for j in range(n)]
                if str_menu == "fill":
                    input_array(matrixA)
                elif str_menu == "random":
                    A = enter_validated_number("Enter A: ", "board")
                    B = enter_validated_number("Enter B: ", "board")
                    if A > B: 
                        A=A+B; 
                        B=A-B; 
                        A=A-B;
                    input_random_from_A_to_B(matrixA, A, B)
            except ValueError as message:
                print(str(message))
                continue

        matrixB = build_matrixB(matrixA)

        print("\n\n  MATRIX A")
        print_array(matrixA)

        print("  RESULT: MATRIX B")
        print_array(matrixB)


menu()
