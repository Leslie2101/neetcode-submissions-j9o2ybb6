class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # keep track of available projects 
        available = []
        projects = sorted(range(len(profits)), key=lambda x: (capital[x], -profits[x]))

        print(projects)
        # load available projects
        i = 0
        while i < len(projects) and capital[projects[i]] <= w:
            heapq.heappush(available, -profits[projects[i]])
            i += 1

        print(i, available)

        # choose best profit greedily
        cnt = 0
        while available and cnt < k:

            # select best profit from qualified project 
            profit = -heapq.heappop(available)
            w += profit
            cnt += 1


            # load qualified project
            while i < len(projects) and capital[projects[i]] <= w:
                heapq.heappush(available, -profits[projects[i]])
                i += 1

            
        
        return w

            
            



