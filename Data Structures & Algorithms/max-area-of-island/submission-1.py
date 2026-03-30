class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        deltas = [(0,1), (0,-1), (1,0), (-1,0)]
        def bfs(sr, sc):
            queue = deque([(sr,sc)])
            cnt = 0

            while queue:
                r, c = queue.popleft()
                
                if grid[r][c] == 0:
                    continue

                grid[r][c] = 0
                cnt += 1

                for dx, dy in deltas:
                    newR, newC = dx+r, dy+c
                    if newR >= 0 and newR < len(grid) and newC >= 0 and newC < len(grid[0]):
                        if grid[newR][newC] == 1:
                            queue.append((newR, newC))

            return cnt
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i,j))
        
        return maxArea


                 