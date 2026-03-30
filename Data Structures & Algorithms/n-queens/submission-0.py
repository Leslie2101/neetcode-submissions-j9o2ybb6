class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        res = []


        def makeBoard(prevQueens):
            board = [['.']*n for _ in range(n)]

            for i,j in prevQueens:
                board[i][j] = 'Q'
                board[i] = "".join(board[i])
            
            return board
        
        def check(prevQueens, coord):
            
            # check if coord violate previous queens 
            # check by diagonal and by x, y

            x, y = coord
            for prevX, prevY in prevQueens:
                if x == prevX or y == prevY or abs(x-prevX) == abs(y-prevY):
                    return False 

            return True


        # try backtrack to place each queen in each row
        # check with previous placed queens so far 
        def backtrack(row, prevQueens):
            
            if row == n:
                res.append(makeBoard(prevQueens))
                return 

              

            # try place in each column
            for col in range(n): 

                # check if it violate previous queens columns 
                if check(prevQueens, (row,col)):
                    prevQueens.append((row,col))
                    
                    backtrack(row+1, prevQueens)

                    prevQueens.pop()
            

        backtrack(0, deque())

        return res