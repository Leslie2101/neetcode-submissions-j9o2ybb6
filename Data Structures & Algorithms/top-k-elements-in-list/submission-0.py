class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freqs = [[] for _ in range(len(nums)+1)]
        for key, val in counter.items():
            freqs[val].append(key)
        
        res = []
        for i in range(len(freqs)-1, -1, -1):
            for key in freqs[i]:
                res.append(key)
            
                if len(res) == k:
                    return res
        
        return res