def InplaceHeapSort(queue):
    for i in range(len(queue)):
        CI = i
        while (CI > 0):
            PI = (CI - 1) // 2
            if queue[ CI ] < queue[ PI ]:
                queue[ CI ], queue[ PI ] = queue[ PI ], queue[ CI ]
            else:
                break

            CI = PI
    print(queue)

    if len(queue) == 0:
        return None

    size = len(queue)

    while size > 0:
        queue[ 0 ], queue[ size - 1 ] = queue[ size - 1 ], queue[ 0 ]
        size -= 1
        PI = 0
        while True:
            LCI = 2 * PI + 1
            RCI = 2 * PI + 2
            min_idx = PI

            if LCI < size and queue[ LCI ] < queue[ min_idx ]:
                min_idx = LCI
            if RCI < size and queue[ RCI ] < queue[ min_idx ]:
                min_idx = RCI

            if PI == min_idx:
                break

            queue[ PI ], queue[ min_idx ] = queue[ min_idx ], queue[ PI ]

            PI = min_idx
    print(queue)


a = [ 3, 5, 1, 2, 6, 8, 0, 9,-4 ]
InplaceHeapSort(a)
