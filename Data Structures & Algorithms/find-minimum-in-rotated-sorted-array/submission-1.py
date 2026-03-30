import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0
        h = len(nums) - 1
        ans = math.inf 

        while l <= h:
            mid = (l+h)//2

            if nums[mid] >= nums[l]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                ans = min(ans, nums[mid])
                h = mid - 1

        return ans

                