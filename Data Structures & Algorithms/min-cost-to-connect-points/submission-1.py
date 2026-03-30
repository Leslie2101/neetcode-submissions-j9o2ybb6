class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # idea:
        # chooose edge with minimum cost each time - check if the edge does not connect 2 connected points 
        # stop when number of edges added is n-1


        n = len(points)
        parents = list(range(n))
        ranks = [0]*n 

        def find(i):
            par = parents[i]

            if par != parents[par]:
                parents[par] = find(par)
                return parents[par]
            
            return par 
        
        def unite(i, j):
            irep = find(i)
            jrep = find(j)

            if irep == jrep:
                return False 
            
            if ranks[irep] < ranks[jrep]:
                parents[irep] = jrep
            elif ranks[irep] > ranks[jrep]:
                parents[jrep] = irep
            else:
                parents[jrep] = irep
                ranks[irep] += 1
            
            return True
        
        # add edges to pq
        pq = [] 
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(pq, (dist, i, j))
        
        cnt = 0
        cost = 0
        while cnt < n-1:
            dist, i, j = heapq.heappop(pq)

            if unite(i, j):
                print("merge: ", points[i], points[j], dist)
                cnt += 1
                cost += dist 

        return cost
            
        