class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        # between the current set and the current interval
        # select the one with smaller right end 
        
        removed = 0
        l = r = None 

        for start, end in intervals:
            if l == None:
                l = start
                r = end 
            elif start < r:
                removed += 1
            else:
                l = start 
                r = end 
        
        return removed

