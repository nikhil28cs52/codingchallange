class Solution:
    def knapsack(self, weight, price, C):
        n = len(price)

        dp = [[0 for _ in range(C+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(C+1):
                if i ==0 or j == 0:
                    dp[i][j]=0
                elif weight[i-1]>C:
                    dp[i][j]=dp[i-1][j]
                else:
                    inc = price[i-1] + dp[i-1][j-weight[i-1]]
                    exc = dp[i-1][j]
                    dp[i][j] = max(inc,exc)

        return dp[n][C]


B = [10, 20, 30]
A = [60, 100, 120]

C = 50

obj = Solution()
print(obj.knapsack(B,A,C))