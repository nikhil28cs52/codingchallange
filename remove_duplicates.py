def remove_duplicates(A):
    n = len(A)
    lst = [ ]
    for i in range(n):
        if lst.count(A[ i ]) == 0:
            lst.append(A[ i ])

    return lst


Array = [ 2, 6, 3, 4, 24, 4, 7, 1, 2, 6, 3, 0, 9 ]

print(remove_duplicates(Array))
