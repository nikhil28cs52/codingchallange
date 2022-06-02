def len_arr(string):
    if len(string) == 0:
        return 0

    rec = len_arr(string[ 1: ])
    return 1 + rec


if __name__ == '__main__':
    A = "bcdrg"
    print(len_arr(A))
