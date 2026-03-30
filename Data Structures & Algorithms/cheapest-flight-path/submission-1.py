class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dfs to find the path from src to dst 

        # get adjList
        adjList = defaultdict(lambda: {})
        for from_i, to_i, price_i in flights:
            adjList[from_i][to_i] = price_i

        visited = set()
        def dfs(cur: int, nodeCnt: int, cost: int):
            nodeCnt += 1

            # process the node
            if nodeCnt - 2 > k:
                return math.inf 

            if cur == dst and nodeCnt - 2 <= k:
                return cost 

            # marked as visited 
            visited.add(cur)

            res = math.inf
            # explore children 
            for child in adjList[cur]:
                if child not in visited:
                    res = min(res, dfs(child, nodeCnt, cost + adjList[cur][child]))


            # unmarked from visited 
            visited.remove(cur)
            return res
        
        res = dfs(src, 0, 0) 
        if res != math.inf:
            return res
        
        return -1