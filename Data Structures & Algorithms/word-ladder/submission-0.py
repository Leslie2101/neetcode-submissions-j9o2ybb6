class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # construct graph
        wordList = list(set(wordList))
        wordList.append(beginWord)

        if endWord not in wordList:
            return 0

        adjList = defaultdict(list)

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):

                # check diff 
                countDiff = 0
                for k in range(len(wordList[i])):
                    if wordList[i][k] != wordList[j][k]:
                        countDiff += 1
                    
                    if countDiff > 1:
                        break 
                
                if countDiff == 1:
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])
        
        # do BFS to find minimum transformation
        queue = deque([(beginWord,1)])
        visited = set()
        while queue:
            word, step = queue.popleft()

            if word in visited:
                continue
            
            if word == endWord:
                return step

            visited.add(word)
            
            for adj in adjList[word]:
                if adj not in visited:
                    queue.append((adj, step + 1))

        return 0
            



