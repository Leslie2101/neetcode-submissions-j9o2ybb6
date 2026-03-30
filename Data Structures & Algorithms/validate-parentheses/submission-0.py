class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        closingsMap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for ch in s:
            if ch in closingsMap:
                stack.append(ch)
            else:
                if not stack or closingsMap[stack[-1]] != ch:
                    return False 
                stack.pop()
        
        return len(stack) == 0