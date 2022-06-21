def fib2(A, lst):
    if A == 0 or A == 1:
        return A
    if lst[ A ] != 0:
        return lst[ A ]

    ans = fib2(A - 1, lst) + fib2(A - 2, lst)
    lst[ A ] = ans
    print(ans)
    return ans


def fib3(n):
    if n ==0 or n ==1:
        return n
    A = [ 0 ]*(n+1)
    A[1]=1
    for i in range(2, n+1):
        A[ i ] = A[ i -1] + A[i-2]
        print(A[ i ])

    ans = A[ i ]
    return ans


print(fib3(1))
