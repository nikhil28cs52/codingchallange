def partition(A, s, e):
    pivot = A[ e ]
    i = s
    for j in range(s, e):
        if not (A[j] > pivot) :  # if curent elemt greater than pivot Do nothing else swap i and j
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[e] = A[e], A[i]

    return i


def quick_sort(A, s, e):
    if s > e:
        return

    q = partition(A, s, e)
    print(q)
    quick_sort(A, s, q - 1)
    quick_sort(A, q + 1, e)


if __name__ == '__main__':
    A = [ 1, 4, 1, 2, 3,2,7,0,12,7,2 ]
    quick_sort(A, 0, len(A) - 1)
    print(A)