def to_s(lst):
    return "".join(lst)


def permutation(s, l, r):
    if l == r:
        print(to_s(s))
    for i in range(l, r + 1):
        s[ l ], s[ i ] = s[ i ], s[ l ]
        permutation(s, l + 1, r)
        s[ l ], s[ i ] = s[ i ], s[ l ]


if __name__ == '__main__':
    str = "ABC"
    a=list(str)
    permutation(a, 0, len(a) - 1)
