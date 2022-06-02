def First_Last_element(A, Key, bool):
    s = 0
    e = len(A) - 1
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if A[ mid ] == Key:
            ans = mid
            if bool :
                e=mid-1
            else:
                s = mid+1

        elif A[ mid ] < Key:
            s = mid + 1
        else:
            e = mid - 1

    return ans


if __name__ == '__main__':
    A = [ 1, 2, 3, 5, 8,8,8, 9 ]

    first = First_Last_element(A, 8,True)
    print(first)
    if first == -1 :
        B= [-1,-1]

    else :
        last = First_Last_element(A, 8,False)
        print(last)
        B= [first,last]

    print(B)