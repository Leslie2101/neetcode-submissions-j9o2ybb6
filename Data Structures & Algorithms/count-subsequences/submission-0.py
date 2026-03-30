from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        # backtrack

        @cache
        def backtrack(sString, tString):

            if not tString:
                return 1
            
            res = 0
            for i in range(len(sString)):
                ch = sString[i]

                if ch == tString[0]:
                    res += backtrack(sString[i+1:], tString[1:])

            return res

        res = backtrack(s, t)
        return res