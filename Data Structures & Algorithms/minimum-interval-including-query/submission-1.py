class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # line sweeping by events 
        events = []
        START, QUERY, END = 0, 1, 2
        for i in range(len(intervals)):
            left, right = intervals[i]
            events.append((left, START, i))
            events.append((right, END, i))
        
        for i in range(len(queries)):
            events.append((queries[i], QUERY, i))
        
        events.sort()

        # process each event
        dropped = [False]*len(intervals)
        res = [-1]*len(queries)

        heap = [] 
        for _, typ, idx in events:
            if typ == START:
                l, r = intervals[idx]
                heapq.heappush(heap, (r-l+1, idx))
            elif typ == END:
                dropped[idx] = True 
            else:

                # remove outdated interval
                while heap and  dropped[heap[0][1]]:
                    drop = heapq.heappop(heap)
                if heap:
                    res[idx] = heap[0][0]
        
        return res
                

