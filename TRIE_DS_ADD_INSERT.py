# insert the word in Trie Data structure

def add(data, root):
    n = len(data)

    for i in range(n):
        idx = ord(data[ i ]) - 65
        if root.child[ idx ] is None:
            root.child[ idx ] = Trie()
            print('{} is inserted first time in Trie'.format(data[ i ]))
        else:
            print('{} is already inserted in Trie'.format(data[ i ]))
        root = root.child[ idx ]
    root.isTerminal = True


def search(data, root):
    n = len(data)

    for i in range(n):
        idx = ord(data[ i ]) - 65
        if root.child[ idx ] is None:
            return False
        else:
            root = root.child[ idx ]
    return root.isTerminal


class Trie:
    def __init__(self):
        self.isTerminal = False
        self.child = [ None ] * 26


lst = [ "NAME", "NIKHIL", "NIKI" ]

root = Trie()
for i in range(len(lst)):
    add(lst[ i ], root)

print(search('NIKI',root))
print(search('AIKI',root))
print(search('NAAME',root))
print(search('NAME',root))
print(search('NIKHIL',root))
