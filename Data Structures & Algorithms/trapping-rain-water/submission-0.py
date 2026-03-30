class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        rightMax = [0]


        for i in range(len(height)):
            leftMax.append(max(leftMax[-1], height[i]))
            rightMax.append(max(rightMax[-1], height[len(height) - i - 1]))
        
        rightMax = rightMax[::-1]

  

        prevWater = 0
        maxWater = 0
        for i in range(len(height)):
            water = prevWater + max((min(leftMax[i], rightMax[i+1]) - height[i]), 0)
            maxWater = max(water, maxWater)
            prevWater = water
        
        return maxWater
