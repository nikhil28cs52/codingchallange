def add(data, root):
    n = len(data)

    for i in range(n):
        idx = ord(data[ i ]) - 97

        if root.child[ idx ] is None:
            root.child[ idx ] = Trie()
        else:
            root.isTerminal = False
        print(data[i],root.isTerminal)
        root = root.child[ idx ]


def search(data, root):
    n = len(data)
    str = ""
    for i in data:
        idx = ord(i) - 97
        if root.child[idx].isTerminal :
            str += i
            print(root.child[idx].isTerminal, i,str)
            return str
        else:
            str += i
            print(root.child[idx].isTerminal, i,str)
        root = root.child[ idx ]
    return str


class Trie:
    def __init__(self):
        self.isTerminal = True
        self.child = [ None ] * 26


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        root = Trie()

        for i in A:
            add(i, root)
        lst = [ ]

        for i in A:
            lst.append(search(i, root))

        return lst


s = Solution()
A = [ "zebra", "dog", "duck" ,"dove" ]
x = s.prefix(A)
print(x)
