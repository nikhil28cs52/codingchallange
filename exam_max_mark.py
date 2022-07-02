def calculation(arr,n):

    arr = sorted(arr)
    j = 0
    for i in range(1,n):
        if arr[i] == arr[i-1]:
