class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i]: max money considered at index i 
        n = len(nums)
        dp_take0 = [0]*n
        dp_not0 = [0]*n 

        dp_take0[0] = nums[0]

        for i in range(1, n-1):
            dp_take0[i] = max(dp_take0[i-1], nums[i] +( dp_take0[i-2] if i-2 >= 0 else 0))
            dp_not0[i] = max(dp_not0[i-1], nums[i] + (dp_not0[i-2] if i-2 >= 0 else 0))
        
        print(dp_take0)
        print(dp_not0)
        # consider last index 
        dp_take0[n-1] = dp_take0[n-2]
        dp_not0[n-1] = max(dp_not0[n-2], nums[n-1] + (dp_not0[n-3] if n-3>=0 else 0)) # consider taking at n-1

        return max(dp_take0[n-1], dp_not0[n-1])



