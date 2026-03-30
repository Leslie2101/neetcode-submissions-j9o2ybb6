class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxVal = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            maxVal = max(maxVal, (r-l)*min(heights[l], heights[r]))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxVal