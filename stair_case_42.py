def staircase(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


if __name__ == '__main__':
    print(staircase(4))
