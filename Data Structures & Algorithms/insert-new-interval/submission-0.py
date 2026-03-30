import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the insertion point 
        idx = bisect.bisect_left(intervals, newInterval)
        intervals = intervals[:idx] + [newInterval] + intervals[idx:]

        # merge intervals 
        res = []

        left = right = None 
        for start, end in intervals:
            if left == None:
                left = start
                right = end 
            
            elif start <= right:
                right = max(end, right)
            else:
                # insert previous segment 
                res.append([left, right])
                left = start
                right = end 
        
        if left != None:
            res.append([left, right])
        return res
