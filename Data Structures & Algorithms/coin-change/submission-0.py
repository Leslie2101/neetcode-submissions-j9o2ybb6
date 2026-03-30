class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: minimum coins for achieving amount i 
        # dp[i] = min(dp[i-j] + 1) for j in coins

        dp = [math.inf]*(amount+1)
        dp[0] = 0

        for val in range(1, amount+1):
            for coin in coins:
                if val - coin >= 0:
                    dp[val] = min(dp[val-coin] + 1, dp[val])
        

        return dp[amount] if dp[amount] != math.inf else -1
    