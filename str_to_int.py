def int2str(input,n):
    if n==0:
        return 0

    smallAns = int2str(input,n-1)
    last_digit = ord(input[n-1]) - ord('0')
    ans = smallAns*10 + last_digit

    return ans


if __name__ == '__main__':

    inp = input()
    print(int2str(inp,len(inp)))