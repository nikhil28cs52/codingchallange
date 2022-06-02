def KSortedArray(A, k):
    n = len(A)
    pq = [ ]
    for i in range(k):
        pq.append(A[ i ])

    for j in range(k, n):
        element = max(pq)
        pq.remove(element)
        pq.append(A[ j ])
        A[ j ] = element

    while k > 0:
        element = max(pq)
        pq.remove(element)
        A[n-k] = element
        k -= 1


A = [ 10, 12, 6, 7, 9 ]
KSortedArray(A, 3)
print(A)