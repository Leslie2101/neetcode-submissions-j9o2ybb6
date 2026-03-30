from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        
        @cache
        def dfs(l, r):
            # l as the left bound and r as the right bound
            # nums i will fall within these as the last element 


            if r < l:
                return 0
            
            lftVal = nums[l-1] if l-1 >= 0 else 1 
            rgtVal = nums[r+1] if r+1 < len(nums) else 1
            
            maxVal = 0
            for i in range(l, r+1):
                score = nums[i] * lftVal * rgtVal
                leftRange = dfs(l, i-1)
                rightRange = dfs(i+1, r)
                maxVal = max(maxVal,  leftRange + rightRange + score)
            
            return maxVal
                

        return dfs(0, len(nums)-1)

