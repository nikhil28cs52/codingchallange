def last_index(A, n,x):
    if n == 0 :
        return

    if A[n-1] == x:

        print(n)

    return last_index(A[:n-1], n-1,x)


if __name__ == '__main__':
    A = [3,4,8,1,2,9,0,2]

    print(last_index(A, 8,2))