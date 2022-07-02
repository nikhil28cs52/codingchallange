'''Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
 If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell
(i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected
(i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.'''


class Node:
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        grid_mat = [[False for _ in range(n)] for _ in range(n)]

        queue = []

        if grid[0][0] == 1:
            return -1

        queue.append(Node(0, 0, 1))
        grid_mat[0][0] = True

        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [1, 1, 1, 0, 0, -1, -1, -1]

        while len(queue) != 0:
            t = queue.pop(0)
            grid_mat[t.x][t.y] = True

            if t.x == n - 1 and t.y == n - 1:
                return t.count

            for i in range(8):
                x = t.x + dx[i]
                y = t.y + dy[i]
                dist = t.count + 1
                if (x < n) and (y < n) and (x >= 0) and (y >= 0) and (grid[x][y] == 0) and (grid_mat[x][y] is False):
                    queue.append(Node(x, y, dist))


grid_matrix = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

s = Solution()
print(s.shortestPathBinaryMatrix(grid_matrix))


#64/89 test case passed