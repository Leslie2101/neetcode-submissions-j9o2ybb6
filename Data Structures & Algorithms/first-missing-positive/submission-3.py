class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue 

            idx = nums[i] - 1
            if nums[i] != nums[idx]:
                # swap 
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i+1
        
        return len(nums) + 1