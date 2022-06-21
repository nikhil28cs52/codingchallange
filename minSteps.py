def minSteps(n):
    if n <= 1:
        return 0

    x = minSteps(n - 1)
    y = pow(2, 10)
    z = pow(2, 10)

    if n % 3 == 0:
        y = minSteps(n // 3)

    if n % 2 == 0:
        z = minSteps(n // 2)

    ans = min(x, y, z)+1

    return ans


n = int(input())
print(minSteps(n))
