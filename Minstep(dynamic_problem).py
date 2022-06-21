def helper(n, Arr):
    if n <= 1:
        return 0
    if Arr[ n ] != -1:
        return Arr[ n ]

    x = helper(n - 1, Arr)
    y = 10000000000
    z = 10000000000

    if n % 3 == 0:
        y = helper(n // 3, Arr)

    if n % 2 == 0:
        z = helper(n // 2, Arr)

    ans = min(x, y, z) + 1
    Arr[ n ] = ans
    return ans


def minSteps(n):
    A = [ -1 ] * (n + 1)
    return helper(n, A)


n = int(input())
print(minSteps(n))
