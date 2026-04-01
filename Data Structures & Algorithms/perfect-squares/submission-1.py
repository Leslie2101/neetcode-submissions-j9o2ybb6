import math
class Solution:
    def numSquares(self, n: int) -> int:
        
        # dp[i]: least number of perfect squares making i
        dp=[math.inf]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            sqr = int(math.sqrt(i))
            if sqr*sqr == i:
                dp[i] = 1
            else:
                for j in range(1, sqr+1):
                    dp[i] = min(dp[i], 1 + (dp[i-j*j]))
        return dp[n]

    