import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track of biggest positive, smallest negative 
        pos = 1
        neg = None

        res = -math.inf 

        for num in nums:

            res = max(res, num)

            if num > 0:
                pos = pos * num if pos != None else num
                neg = neg * num if neg != None else None 

            elif num == 0:
                pos = neg = None 

            else:
                newneg = pos * num if pos != None else num 
                newpos = neg * num if neg != None else None
                pos, neg = newpos, newneg
                
            
                    
            res = max(res, num)
            if pos != None: res = max(res, pos)
            if neg != None: res = max(res, neg)

            print("num", num, "pos", pos, "neg", neg, "res", res)
        
        return res

