class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        maxLen = defaultdict(lambda: math.inf)

        for left, right in intervals:
            for i in range(left, right+1):
                maxLen[i] = min(maxLen[i], right-left+1)
        
        res = []
        for query in queries:
            res.append(maxLen[query] if maxLen[query] < math.inf else -1)
        
        return res

        
