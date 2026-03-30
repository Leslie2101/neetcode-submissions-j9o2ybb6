class TrieNode:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = {}

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.insertWord(word)

    def insertWord(self, word: str):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.isEnd = True 



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie(words)
        print(trie.root.children)
        
        
        deltas = [(-1,0), (1,0), (0,-1), (0,1)]
        res = set()

        words = set(words)
        def backtrack(i, j, visited, currentWord, node):

            

            if board[i][j] not in node.children:
                return 
            

            currentWord += board[i][j]
            node = node.children[board[i][j]]

            if node.isEnd:
                res.add(currentWord)

            visited.add((i,j))

            for dx, dy in deltas:
                newX, newY = i+dx, j+dy

                if newX >= 0 and newX < len(board) and newY >= 0 and newY < len(board[0]):
                    if (newX, newY) not in visited:
                        backtrack(newX, newY, visited, currentWord, node)
            
            visited.remove((i,j))
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                backtrack(i,j, visited, "", trie.root)
        
        return list(res)

            


