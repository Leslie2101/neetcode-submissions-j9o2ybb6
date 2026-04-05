class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        doable = [False]*len(s)

        if s[-1] == '1':
            return False

        doable[len(s)-1] = True 

        for i in range(len(s)-2, -1, -1):
            if s[i] == '1':
                doable[i] = False 
            else:
                for j in range(min(i + maxJump, len(s)-1), i+minJump-1, -1):
                    if doable[j]:
                        doable[i] = True 
                        break 
            
        return doable[0]
