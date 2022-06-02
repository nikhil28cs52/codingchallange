def selection_sort(A):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[ j ] < A[ i ]:
                A[ j ], A[ i ] = A[ i ], A[ j ]
    print("selection sort  : {}".format(A))


def bubble_sort(A):
    for i in range(len(A) - 1):
        flag = 0
        for j in range(len(A) - 1):
            if A[ j + 1 ] < A[ j ]:
                A[ j ], A[ i ] = A[ i ], A[ j ]
                flag = 1

        if flag == 0:
            print("already sorted")
            break
    print("bubble sort     : {}".format(A))


if __name__ == '__main__':
    A = [ 1,2,3,4,5,6]

    selection_sort(A)
    bubble_sort(A)
