class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = deque()
        maxArea = 0

        for i in range(len(heights) + 1):
            
            height = heights[i] if i < len(heights) else 0
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i-1 - stack[-1] if stack else i
                maxArea = max(h*w, maxArea)

            stack.append(i)
        return maxArea
