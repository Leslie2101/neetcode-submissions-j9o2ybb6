class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total = sum(nums)

        def achievable(mid):
            # check if its possible to achieve max sum among k subarrays <= mid 
            # greedily make long arr < k, check if the total cnt <= mid
            cnt = 0
            cur = 0

            for num in nums:
                cur += num 

                if num > mid:
                    return False 

                if cur > mid:
                    cnt += 1
                    cur = num


            
            cnt += 1
            # print("check", mid, cnt)
            return cnt <= k


        low = 0
        high = total
        ans = high
        while low <= high:
            mid = (low + high)//2
            # print("access", mid)

            if achievable(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
