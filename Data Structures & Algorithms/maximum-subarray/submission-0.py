class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEnding = 0
        res = -math.inf

        for num in nums:
            maxEnding = max(maxEnding + num, num)
            res = max(res, maxEnding)
        
        return res
