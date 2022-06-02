def toh(n):
    if n == 0:
        return 0

    return toh(n - 1) + 1 + toh(n - 1)


def print_step(n, s, d, h):
    if n == 0:
        return

    print_step(n - 1, s, h, d)
    print("Moving Disk {} from {} to {}".format(n,s, d))
    print_step(n - 1, h, d, s)


if __name__ == '__main__':
    n = int(input())
    print(toh(n))
    print(print_step(n, 'A', 'C', 'B'))
