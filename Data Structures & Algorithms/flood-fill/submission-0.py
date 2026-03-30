class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        startingColor = image[sr][sc]

        if startingColor == color:
            return image

        queue = deque([(sr, sc)])
        deltas = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            r, c = queue.popleft()

            if image[r][c] != startingColor:
                continue 

            image[r][c] = color 

            for dx, dy in deltas:
                x, y = r+dx, c+dy

                if x >= 0 and x < len(image) and y >= 0 and y < len(image[0]):
                    if image[x][y] == startingColor:
                        queue.append((x,y))
        
        return image
