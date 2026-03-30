from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)

        @cache
        def dfs(word):

            if not word:
                return []

            res = []
            if word in wordDict:
                res = [word]

            string = ""
            for i in range(len(word)):
                string += word[i]
                if string in wordDict: 
                    remains = dfs(word[i+1:])
                    if remains:
                        for remain in remains: 
                            res.append(string + " " + remain)
            
            return res

        res = dfs(s)
        print(res)

        return res



