from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        @cache
        def helper(s: str) -> bool: 
            if (not s) or (s in wordDict):
                return True

            for i in range(1, len(s)):
                fst = s[:i]
                snd = s[i:]

                if helper(fst) and helper(snd):
                    return True

            return False 
        

        return helper(s)
