class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixMin = 0
        curPrefix = 0
        res = -math.inf

        for num in nums:
            curPrefix += num

            res = max(res, curPrefix - prefixMin)
            prefixMin = min(curPrefix, prefixMin)

        
        return res
