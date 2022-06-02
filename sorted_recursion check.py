def sorted(A, n):
    if n == 0 or n == 1:
        return True

    elif A[0] > A[1]:
        return False
    else:
        return sorted(A[1:], n-1)


if __name__ == '__main__':
    A = [0,1,1,1,8,0,3]

    print(sorted(A, 7))
