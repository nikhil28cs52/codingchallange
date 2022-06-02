# using Priority Queue we can reduce the time complexity n logn to nlogk which is much better

from Priority_queue import PriorityQueue  # user defined file


def KsmallestElement(A, k):
    n = len(A)
    pq = []
    for i in range(k):
        pq.append(A[ i ])

    for j in range(k, n):
        if A[ j ] < max(pq):
            pq.remove(max(pq))
            pq.append(A[ j ])

    print(pq)


B = [ 7, 2, 9, 11, 0, 3, 6, 0, 99, 8, 4, 100, -5 ]

KsmallestElement(B,3)
