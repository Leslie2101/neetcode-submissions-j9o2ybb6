from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # dp_inc[i][j] = longest path ending with current square[i][j] and the array is incr
        # dp_dec[i][j] = longest path ending with current square[i][j] and the array is decr

        # dp_inc[i][j] = max(dp_inc[i-1][j] if mat[i-1][j] < mat[i][j],
        #                     dp_inc[i][j-1] if mat[i][j-1] < mat[i][j])


        @cache
        def dfs(r, c):

            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                return 0

            # mark the node 
            cnt = 1

            # explore its adj neighbors 
            extra = max(
                dfs(r+1, c) if r+1 >= 0 and r+1 < len(matrix) and matrix[r+1][c] > matrix[r][c] else 0, 
                dfs(r-1, c) if r-1 >= 0 and r-1 < len(matrix) and matrix[r-1][c] > matrix[r][c] else 0, 
                dfs(r, c-1) if c-1 >= 0 and c-1 < len(matrix[0]) and matrix[r][c-1] > matrix[r][c] else 0, 
                dfs(r, c+1) if c+1 >= 0 and c+1 < len(matrix[0]) and matrix[r][c+1] > matrix[r][c] else 0
            )

            return cnt + extra 

        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i,j))
        
        return res
