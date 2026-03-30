from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def dfs(arr):
            if not arr:
                return 0
            
            maxScore = 0
            for i in range(len(arr)):
                lft = arr[i-1] if i-1 >= 0 else 1
                rgt = arr[i+1] if i+1 < len(arr) else 1
                score = lft * rgt * arr[i]

                maxScore = max(maxScore, score + dfs(tuple(arr[:i] + arr[i+1:])))
                
            return maxScore 
        
        res = dfs(tuple(nums))
        return res
                

