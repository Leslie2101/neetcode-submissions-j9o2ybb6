class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        deltas = [(-1, 0), (1,0), (0, -1), (0, 1)]
        visited = set()
        def backtrack(word_index, x, y):
            
            visited.add((x,y))
            
            res = False 
            if word[word_index] == board[x][y]:

                if word_index == len(word)-1:
                    return True
                # explore other pathway 

                for dx, dy in deltas:
                    newx, newy = x+dx, y+dy
                    if 0 <= newx < len(board) and 0 <= newy < len(board[0]):
                        if (newx, newy) not in visited and backtrack(word_index + 1, newx, newy):
                            return True


            visited.remove((x,y))

            return False 
        


        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0, i, j):
                    return True 
        
        return False 