def isalnum(s):
    if 122 > ord(s) > 65:
        return True
    else:
        return False


def isPalindrome(s1):
    e = len(s1)-1
    s = 0
    while s < e:
        while s1[s].isalnum():
            s += 1
        while s1[e].isalnum():
            e -= 1
        if s1[ s ].lower() != s1[ e ].lower():
            return False

        s+=1
        e-=1
    return True


print(isPalindrome('A man nam a'))
