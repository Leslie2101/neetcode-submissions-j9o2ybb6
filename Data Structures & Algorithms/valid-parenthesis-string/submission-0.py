class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpening = maxOpening = 0

        for ch in s:
            if ch == "(":
                minOpening += 1 
                maxOpening += 1
            elif ch == ")":
                minOpening -= 1
                maxOpening -= 1
            elif ch == "*":
                minOpening -= 1
                maxOpening += 1
            
            if maxOpening < 0:
                return False 

            minOpening = max(minOpening, 0)

        return minOpening == 0 