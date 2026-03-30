from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i, j):
            # check if s[i:] matches p[j:]
            if j == len(p):
                return i == len(s)

            match = False 
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                match = True 
            
            if j+1 < len(p) and p[j+1] == '*':
                if match and dfs(i+1, j) or dfs(i, j+2):
                    return True
                

            # move on to next character             
            if match and dfs(i+1, j+1):
                return True
            
            return False 

        
        res = dfs(0,0)
        return res