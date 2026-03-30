class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isPossible(k: int):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / k)
            
            return cnt <= h
        

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high)//2

            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans 