from functools import cache 
import math
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        @cache
        def callAPI(index):

            if index < 0 or index >= mountainArr.length():
                return -math.inf
            return mountainArr.get(index)

        # find peak first with BS
        low = 0
        high = mountainArr.length() - 1
        peak_index = 0

        while low <= high:
            mid = (low+high)//2

            if callAPI(mid) > callAPI(mid-1) and callAPI(mid) > callAPI(mid+1):
                peak_index = mid
                break
            elif callAPI(mid) > callAPI(mid-1):
                # left side does not contain peak 
                low = mid + 1
            elif callAPI(mid) > callAPI(mid+1):
                high = mid - 1
        
        print(peak_index)

        if callAPI(peak_index) == target:
            return peak_index



        # then find on left portion
        low = 0
        high = peak_index - 1 
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if callAPI(mid) == target:
                ans = mid 
                high = mid - 1
            elif callAPI(mid) > target:
                high = mid - 1
            else:
                low = mid + 1 

        if ans != -1:
            return ans 

        # then find on right portion 
        low = peak_index + 1
        high = mountainArr.length() -1 

        print(low, high)
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if callAPI(mid) == target:
                ans = mid 
                high = mid - 1
            elif callAPI(mid) > target:
                low = mid + 1
            else:
                high = mid - 1 
        return ans