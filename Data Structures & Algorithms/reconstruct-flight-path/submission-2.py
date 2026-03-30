class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        adjList = defaultdict(list)
        tickets = sorted(tickets, reverse=True)

        for src, dest in tickets:
            adjList[src].append(dest)


        res = []
        stack = ["JFK"]

        while stack:
            cur = stack[-1]
            if not adjList[cur]:
                res.append(stack.pop())
            else:
                stack.append(adjList[cur].pop())
        
        return res[::-1]