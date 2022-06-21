def minSteps(n):
    A = [ 0, 0 ]

    for i in range(2, n + 1):

        x = A[ i - 1 ]
        y = 10000000000
        z = 10000000000

        if i % 3 == 0:
            y = A[i//3]

        if i % 2 == 0:
            z = A[i//2]

        ans = min(x, y, z) + 1

        A.append(ans)

    return A[n]


n = int(input())
print(minSteps(n))
