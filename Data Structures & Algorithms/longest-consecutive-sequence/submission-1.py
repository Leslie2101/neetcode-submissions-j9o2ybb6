class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in setNums:
                cur = num
                cnt = 0
                while cur in setNums:
                    cnt += 1
                    cur += 1

                res = max(res, cnt)
            
            else:
                continue 
        
        return res