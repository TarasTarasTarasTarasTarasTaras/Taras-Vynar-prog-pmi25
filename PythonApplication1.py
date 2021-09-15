class MyException(Exception): pass

def input_arr(n, arr):
    print("\n Input " + str(n) + " numbers:")
    for i in range(n):
        arr.append(int(input()))
    return 

def cyclic_shift(k, arr):
    temp_arr = []
    for i in range(k):
        temp_arr.append(arr[i])
    for i in range(len(arr)-k):
        arr[i] = arr[i+k]
    for i in range(k):
        arr[len(arr)-k+i] = temp_arr[i]
    return

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])


while True:
    try:
        n = int(input("Input n: "))
        k = int(input("Input k: (k<n) "))
        
        if(k>=n): raise MyException

        arr = []
        input_arr(n, arr)
        cyclic_shift(k, arr)

        print("\n Print switfed array:")
        print_arr(arr)

    except ValueError:
        print(" SYNTAX ERROR")
        continue

    except MyException:
        print(" ERROR: k should be '<' n")
        continue
    break