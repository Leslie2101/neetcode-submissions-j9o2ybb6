class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = defaultdict(int)
        cols = defaultdict(int)
        groups = defaultdict(int)


        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                row, col = i, j

                group = (row//3, col//3)

                val = int(board[i][j]) - 1

                if (1 << val) & rows[row]:
                    return False 
                
                if (1 << val) & cols[col]:
                    return False 
                
                if (1 << val) & groups[group]:
                    return False

                

                rows[row] |= (1<<val)
                cols[col] |= (1<<val)
                groups[group] |= (1<<val)

        
        
        return True 