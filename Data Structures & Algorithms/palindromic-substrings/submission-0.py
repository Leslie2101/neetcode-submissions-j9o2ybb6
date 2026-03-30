class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def findPalinMax(i: int, j: int):
            res = -1 if i == j else 0
            l, r = i, j
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 2
                l -= 1
                r += 1
            
            return res



        # find longest palindrom for each character in s as a center 
        res = 0
        for i in range(len(s)):
            print(i, s[i])
            oddPalin = findPalinMax(i, i)
            res += oddPalin//2 + 1
            if i + 1 < len(s) and s[i] == s[i+1]:
                evenPalin = findPalinMax(i, i+1)
                res += evenPalin // 2 
            # the longest palindrom will give extra l//2 palindrom strings
                print(f"{oddPalin=}, {evenPalin=}")
        
        return res


