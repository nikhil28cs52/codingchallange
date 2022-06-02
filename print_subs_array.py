def Print_subs_array(input,output):
    if len(input) == 0:
        print(output)
        return

    Print_subs_array(input[1:], input[0] + output )
    Print_subs_array(input[ 1: ], output)


def Print_subs_array_2(input,output,lst):
    if len(input) == 0:
        lst.append(output)
        return

    Print_subs_array_2(input[1:], input[0] + output ,lst)
    Print_subs_array_2(input[ 1: ], output,lst)


if __name__ == '__main__':
    output=""
    input = input()
    lst=[]
    Print_subs_array_2(input,output,lst)
    print(lst)
    print(len(lst))

