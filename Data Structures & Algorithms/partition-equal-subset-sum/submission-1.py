class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        # find partition possible by checking if any combination made total//2
        # dp[i][j]: is it possible to make sum of j considering i first elements 
        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[j]]

        dp = [[False]*(total//2+1) for _ in range(len(nums)+1)]
        dp[0][0] = True 


        for i in range(1, len(nums)+1):
            dp[i][0] = True
            for j in range(1, total//2+1):
                dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i-1]] if j >= nums[i-1] else False)
        print(dp)
        return dp[len(nums)][total//2]
     
        