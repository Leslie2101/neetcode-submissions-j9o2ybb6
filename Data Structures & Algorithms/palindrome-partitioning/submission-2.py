from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        @cache
        def isPalin(string):
            l = 0
            h = len(string)-1

            while l < h:
                if string[l] != string[h]:
                    return False 
                
                l += 1
                h -= 1
            
            return True 

        @cache
        def dfs(i):
            # all splittings for s[i:]
            # if i == len(s)-1:
            #     return [[s[i]]]
            
            if i == len(s):
                return [[]]

            res = []            
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if isPalin(substr):
                    for val in dfs(j+1):
                        res.append([substr] + val)
        
            return res

        res = dfs(0)

        return res