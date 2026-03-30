class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # minimise the maximum value on a path from topleft to bottom right 

        # prioritise explore square with lower elevation 

        heap = [(grid[0][0], 0, 0)]
        visited = set()
        deltas = [(0,1), (0,-1), (1,0), (-1,0)]
    
        maxValue = grid[0][0]
        while heap:
            val, i, j = heapq.heappop(heap)

            maxValue = max(maxValue, grid[i][j])

            if i==len(grid)-1 and j == len(grid[0])-1:
                return maxValue 
            
            visited.add((i,j))

            # explore neighbors
            for dx, dy in deltas:
                x, y = i+dx, j+dy

                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if (x,y) not in visited:
                        heapq.heappush(heap, (grid[x][y], x, y))
        
        return maxValue
            

