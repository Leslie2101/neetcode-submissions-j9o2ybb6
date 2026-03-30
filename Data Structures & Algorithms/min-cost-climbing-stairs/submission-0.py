class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp[i] = min cost to reach i-th floor 
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        n = len(cost)
        dp = [math.inf]*(n+1)
        dp[0]=dp[1]= 0 # starting points 

        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]