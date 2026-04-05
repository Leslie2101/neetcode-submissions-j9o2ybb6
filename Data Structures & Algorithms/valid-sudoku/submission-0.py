class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = defaultdict(set)
        cols = defaultdict(set)
        groups = defaultdict(set)


        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                row, col = i, j

                group = (row//3, col//3)

                if board[i][j] in rows[row] or board[i][j] in cols[col] or board[i][j] in groups[group]:
                    return False 
                

                rows[row].add(board[i][j])
                cols[col].add(board[i][j])
                groups[group].add(board[i][j])

        
        
        return True 