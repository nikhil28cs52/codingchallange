def Binary_search(A, key, s, e):
    if s > e:
        print("Key Not found")
        return

    mid = (s + e) // 2

    if A[ mid ] == key:
        print("Key is found at index {}".format(mid))
        return
    elif A[ mid ] < key:
        s = mid + 1
        Binary_search(A, key, s, e)
    elif A[ mid ] > key:
        e = mid - 1
        Binary_search(A, key, s, e)


if __name__ == '__main__':
    lst = [ int(x) for x in input("Enter the element \n").split() ]
    key = int(input())
    Binary_search(lst, 7, 0, len(lst) - 1)
