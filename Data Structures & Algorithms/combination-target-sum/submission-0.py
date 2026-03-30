class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        lsts = []

        used = []
        def backtrack(i, target):

            if target - nums[i] < 0:
                return 
            
            used.append(nums[i])

            if target - nums[i] == 0:
                lsts.append(used.copy())

        
            for j in range(i, len(nums)):    
                backtrack(j, target - nums[i])
            
            used.pop()

        
        for i in range(len(nums)):
            backtrack(i, target)
        return lsts