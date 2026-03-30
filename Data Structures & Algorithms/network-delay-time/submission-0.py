class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # construct dist and adj dictionary

        dist = defaultdict(int) 
        adj = defaultdict(list)


        for time in times:
            u, v, t = time 

            adj[u].append(v)
            dist[(u, v)] = t       


        # dijkstra

        pq = [(0, k)]

        unvisited = set(list(range(1, n+1)))

        res = -1

        while pq:
            d, u = heapq.heappop(pq)

            if u not in unvisited:
                continue
            

            unvisited.remove(u)

            res = max(res, d)


            for v in adj[u]:
                if v in unvisited:
                    heapq.heappush(pq, (d + dist[(u, v)], v))
        

        if unvisited:
            return -1
        

        return res


