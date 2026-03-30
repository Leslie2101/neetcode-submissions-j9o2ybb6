class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible = [False]*len(nums)
        possible[0] = True
        
        for i in range(len(nums)):
            # is this tile reachable? 
            if possible[i]:
                for j in range(i+1, min(nums[i] + i + 1, len(nums))):
                    possible[j] = True 
            else:
                continue 

            

        return possible[-1]
        