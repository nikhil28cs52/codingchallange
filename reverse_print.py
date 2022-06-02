def reverse(string):
    if len(string) == 0:
        return
    return string[0]+ reverse(string[ 1: ])


if __name__ == '__main__':
    A = "Nikhil"

    print(reverse(A))
