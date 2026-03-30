class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            # if the goal tile can be reached?
            if i + nums[i] >= goal:
                goal = i 
        
        return nums[0] >= goal
        