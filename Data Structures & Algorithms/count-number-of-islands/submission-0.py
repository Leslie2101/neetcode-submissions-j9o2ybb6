class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        def bfs(i: int, j: int)->None:
            queue = deque([(i,j)])
            while queue:
                x, y = queue.popleft()

                if grid[x][y] == '0':
                    continue

                grid[x][y] = '0'

                deltas = [(-1, 0), (1, 0), (0, 1), (0,-1)]

                for dx, dy in deltas:
                    newX, newY = x+dx, y+dy

                    if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]):
                        if grid[newX][newY] == '1':
                            queue.append((newX, newY))


            
        

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        
        return res