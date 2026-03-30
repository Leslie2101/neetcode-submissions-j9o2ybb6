class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]: max length subsequence ending with nums[i]
        n = len(nums)
        dp = [1]*n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            res = max(res, dp[i])
        
        return res
        
        