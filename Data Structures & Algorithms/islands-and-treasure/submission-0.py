class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j, 0))
        
        deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
        # fill squares with nearest treasure
        while queue:
            x, y, step = queue.popleft()

            if grid[x][y] > 0 and grid[x][y] < INF:
                continue

            grid[x][y] = step

            for dx, dy in deltas:
                newx, newy = dx+x, dy+y


                if newx < len(grid) and newx >= 0 and newy >= 0 and newy < len(grid[0]):
                    if grid[newx][newy] == INF:
                        queue.append((newx, newy, step+1))

        return  
            
        