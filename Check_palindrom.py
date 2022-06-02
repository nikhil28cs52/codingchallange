def check_pal(A, s, e):
    if s>e:
        return True

    if A[s] == A[e]:
        return check_pal(A, s + 1, e - 1)
    else:
        print("false")
        return False


if __name__ == '__main__':
    A = (1, 2, 3, 4, 3, 2, 1)

    print(check_pal(A, 0, 6))
