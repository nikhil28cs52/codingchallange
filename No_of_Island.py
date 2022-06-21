'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3'''


class Solution:
    def dfs(self, grid, i, j, m, n, visited):
        if (i >= m) or (i < 0) or (j < 0) or (j >= n):
            return

        if grid[ i ][ j ] == '0':
            return

        if visited[ i ][ j ] == True:
            return

        visited[ i ][ j ] = True

        self.dfs(grid, i - 1, j, m, n, visited)

        self.dfs(grid, i, j - 1, m, n, visited)

        self.dfs(grid, i, j + 1, m, n, visited)

        self.dfs(grid, i + 1, j, m, n, visited)

    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[ 0 ])

        visited = [ [ False for _ in range(n) ] for _ in range(m) ]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[ i ][ j ] == '1' and (visited[ i ][ j ] == False):
                    print('starting point of dfs start  {} :{}'.format(i,j))
                    self.dfs(grid, i, j, m, n, visited)
                    count += 1
        return count,visited


grid = [["1","1","1","1","1","0","1","1","1","1"],
        ["1","0","1","0","1","1","1","1","1","1"],
        ["0","1","1","1","0","1","1","1","1","1"],
        ["1","1","0","1","1","0","0","0","0","1"],
        ["1","0","1","0","1","0","0","1","0","1"],
        ["1","0","0","1","1","1","0","1","0","0"],
        ["0","0","1","0","0","1","1","1","1","0"],
        ["1","0","1","1","1","0","0","1","1","1"],
        ["1","1","1","1","1","1","1","1","0","1"],
        ["1","0","1","1","1","1","1","1","1","0"]]

s = Solution()
x,y= s.numIslands(grid)
print(x)
for i in range(len(y)):
    print(y[i])