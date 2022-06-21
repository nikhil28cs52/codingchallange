'''Given a set of reviews provided by the customers for different hotels and a string containing Good Words,
you need to sort the reviews in descending order according to their Goodness Value (Higher goodness value first).
We define the Goodness Value of a string as the number of Good Words in that string.

NOTE: Sorting should be stable. If review i and review j have the same Goodness Value then their original order would
be preserved

Example Input
Input 1:

 A = "coolicewifi"
 B = ["wateriscool", "coldicedrink", "coolwifispeed"]


Example Output
Output 1:

 [2, 0, 1]


Example Explanation
Explanation 1:

 sorted reviews are ["coolwifispeed", "wateriscool", "coldicedrink"].'''
from typing import List


def add(data, root):
    n = len(data)

    for i in range(n):
        idx = ord(data[ i ]) - 97
        if root.child[ idx ] is None:
            root.child[ idx ] = Trie()
        root = root.child[ idx ]
    root.isTerminal = True


def search(data, root):
    n = len(data)

    for i in range(n):
        idx = ord(data[ i ]) - 97
        if root.child[ idx ] is None:
            return False
        else:
            root = root.child[ idx ]
    return root.isTerminal


class Trie:
    def __init__(self):
        self.isTerminal = False
        self.child = [ None ] * 26


class Solution:

    def solve(self, A, B):
        A = A.split('_')
        root = Trie()
        for i in range(len(A)):
            add(A[ i ], root)

        lst: List[ int ] = [ ]
        for i in range(len(B)):
            C = B[ i ].split('_')
            count = 0
            for j in range(len(C)):
                x = search(C[ j ], root)
                if x:
                    count += 1
            lst.append([count,i])
        srt = sorted(lst, key=lambda x:x[0],reverse= True)

        d2 = [ item[ 1 ] for item in srt ]
        return d2


A = "cool_ice_wifi"
B = [ "water_is_cool", "cold_ice_drink", "cool_wifi_speed" ]
s = Solution()
x = s.solve(A, B)
print(x)