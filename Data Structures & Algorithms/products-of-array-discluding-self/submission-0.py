class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] *= prefix[i-1] * nums[i]
            suffix[n-i-1] *= suffix[n-i] * nums[n-i-1]
        
        # print(prefix, suffix)
        res = [1]*n

        for i in range(n):
            res[i] = (prefix[i-1] if i-1 >= 0 else 1) * (suffix[i+1] if i+1 < n else 1)

        return res