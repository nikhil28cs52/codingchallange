def R_C_D(A):
    if len(A) == 1:
        return A[ 0 ]

    if A[ 0 ] != A[ 1 ]:
        return A[ 0 ] + R_C_D(A[ 1: ])
    else:
        A = A[ 1: ]
        return R_C_D(A)


if __name__ == '__main__':
    A = "NNNIKKHHILL"
    print(R_C_D(A))
