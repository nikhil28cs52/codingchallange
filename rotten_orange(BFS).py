'''You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
64 OUT OF 82 
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.'''


class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        grid_mat = [[False for _ in range(n)] for _ in range(m)]

        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
                    grid_mat[i][j] = True

        time = 0
        while queue:
            x = queue.pop(0)

            time = max(time, x[2])
            for a, b in ((x[0] - 1, x[1]), (x[0] + 1, x[1]), (x[0], x[1] + 1), (x[0], x[1] - 1)):

                if m > a >= 0 and n > b >= 0 and grid[a][b] == 1 and (not grid_mat[a][b]):
                    queue.append([a, b, x[2] + 1])
                    grid_mat[a][b] = True
                    grid[a][b] = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return time


# test the testcase sample

inp = [[2,1,1],[1,1,0],[0,1,1]]

s=Solution()
print(s.orangesRotting(inp))