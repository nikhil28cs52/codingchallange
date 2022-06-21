def reverse(string):
    if len(string) == 0:
        return ''
    return  reverse(string[ 1: ]) + string[0]


if __name__ == '__main__':
    A = "Nikhil"

    print(reverse(A))
