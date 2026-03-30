class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = deque()
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()

            
            # check if theres a hotter day
            if stack:
                res.append(stack[-1][1]-i)
            else:
                res.append(0)
            
            
            stack.append((temp, i))
        
        return res[::-1]

            