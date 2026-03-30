class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = defaultdict(int)
        prefix = 0
        prefixCount[0] = 1
        res = 0
        for num in nums:
            prefix += num 
            res += prefixCount[prefix - k]
            prefixCount[prefix] += 1
        
        return res