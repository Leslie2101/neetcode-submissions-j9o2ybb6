class Solution:
    

    def longestPalindrome(self, s: str) -> str:
        resLeft = 0
        resLen = 1
        
        def isPalin(leftI, rightI):
            if rightI >= len(s):
                return -1
            
            val = 0
            while  leftI >= 0 and rightI < len(s) and s[leftI] == s[rightI]:
                leftI -= 1
                rightI += 1
                val += 2
            return val


        for l in range(len(s)):
            ans = isPalin(l, l+1)
            print(l, ans)
            if ans > resLen:
                resLeft = l - (ans//2 - 1)
                resLen = ans 

            ans = isPalin(l, l+2) + 1
            if ans > resLen:
                resLeft = l - (ans//2 - 1)
                resLen = ans 

        
        return s[resLeft:resLeft+resLen]