class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 # max profit at house i-1, i-2
        newRob = 0
        for i in range(len(nums)):
            newRob = max(rob1, rob2 + nums[i])
            rob2 = rob1
            rob1 = newRob
        
        return newRob