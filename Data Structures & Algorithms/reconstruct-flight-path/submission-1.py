from sortedcontainers import SortedSet, SortedDict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # make adj list 
        adjList = defaultdict(SortedDict)

        for src, dest in tickets:
            if dest not in adjList[src]:
                adjList[src][dest] = 0

            adjList[src][dest] += 1
        
        visited = set()
        res = []
        def dfs(loc, ticketUsed):
            if ticketUsed == len(tickets):
                return True 
            
            for adj in adjList[loc]:
                if adjList[loc][adj] > 0:

                    adjList[loc][adj] -= 1
                    if dfs(adj, ticketUsed + 1):
                        res.append(adj)
                        return True 
                    adjList[loc][adj] += 1


            return False 

        dfs("JFK", 0)

        return (res+["JFK"])[::-1]


                    


            
