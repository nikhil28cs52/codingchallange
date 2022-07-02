class Solution:

    '''if k =2 means two step allowed
    class Solution:
        def climbStairs(self, n: int) -> int:

            if n ==0 or n == 1:
                return 1
            dp = [0]*(n+1)
            dp[0]=1
            dp[1]=1

            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]

            return dp[n]'''
    def climbStairs(self, n: int) -> int:
        dp =[0]*(n+1)
        dp[0]=1
        dp[1]=1
        k=2
        for i in range(2,n+1):
            ans = 0
            for j in range(1,k+1):
                if i-j >= 0:
                    ans+=dp[i-j]
                    print(ans)
            dp[i]=ans
        print(dp)
        return dp[n]

a = Solution()
a.climbStairs(5)