class Solution:
    def knapsack(self, A, B, C, n):
        if (n == 0) or (C == 0):
            return 0
        if A[n-1] > C:
            return self.knapsack(A, B, C, n - 1)

        inc = B[n - 1] + self.knapsack(A, B, C - A[n - 1], n - 1)

        exc = self.knapsack(A, B, C, n - 1)

        return max(inc, exc)

    def solve(self, A, B, C):
        n = len(A)
        return self.knapsack(A, B, C, n)

B = [10, 20, 30]
A = [60, 100, 120]

C = 50

obj = Solution()
print(obj.solve(B,A,C))