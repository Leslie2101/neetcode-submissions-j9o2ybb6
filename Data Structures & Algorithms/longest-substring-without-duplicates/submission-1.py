class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contained = defaultdict(int)

        l = 0
        r = 0
        res = 0
        while l <= r and r < len(s):
            
            # shift right pointer to max satisfied subarray
            while r < len(s) and contained[s[r]] + 1 <= 1:
                contained[s[r]] += 1
                r += 1

            res = max(res, r-l)

            contained[s[l]] -= 1
            l += 1
        
        return res

