class Solution:

    def helper(self, s1, m, s2, n):

        if m == 0:
            return n
        if n == 0:
            return m

        if s1[m - 1] == s2[n - 1]:
            return self.helper(s1, m - 1, s2, n - 1)

        insert = self.helper(s1, m, s2, n - 1)
        delet = self.helper(s1, m - 1, s2, n)
        replace = self.helper(s1, m - 1, s2, n - 1)

        return 1 + min(insert, delet, replace)

    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        return self.helper(word1, m, word2, n)

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        if m == 0:
            return n
        if n == 0:
            return m

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i][j - 1],
                        dp[i - 1][j]
                    ) + 1

        return dp[m][n]


a = Solution()
print(a.minDistance2('horse', "ros"))



'''Your input
"horse"
"ros"
Output
3
Expected
3 '''
