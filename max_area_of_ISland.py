'''You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.'''


class Solution:
    def dfs(self, grid, i, j, m, n, visited):
        if (i >= m) or (i < 0) or (j < 0) or (j >= n):
            return 0

        if grid[ i ][ j ] == 0:
            return 0

        if visited[ i ][ j ] == True:
            return 0

        visited[ i ][ j ] = True

        return 1 + self.dfs(grid, i - 1, j, m, n, visited) + self.dfs(grid, i, j - 1, m, n, visited) + self.dfs(grid, i,
                                                                                                                j + 1,
                                                                                                                m, n,
                                                                                                                visited) + self.dfs(
            grid, i + 1, j, m, n, visited)

    def maxAreaOfIsland(self, grid) :
        m = len(grid)
        n = len(grid[ 0 ])

        visited = [ [ False for _ in range(n) ] for _ in range(m) ]

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[ i ][ j ] == 1 and (visited[ i ][ j ] == False):
                    area = self.dfs(grid, i, j, m, n, visited)
                    max_area = max(max_area, area)
        return max_area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
x= s.maxAreaOfIsland(grid)
print(x)


