class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        adjList = defaultdict(set)
        charSet = set()

        # top sort
        removed = set()
        starters = set()
        charSet = set(words[0])
        for i in range(len(words)-1):
            fst = words[i]
            snd = words[i+1]
            
            charSet = charSet.union({ch for ch in fst})
            charSet = charSet.union({ch for ch in snd})

            diffI = -1
            for i in range(min(len(fst), len(snd))):
                if fst[i] != snd[i]:
                    starters.add(fst[i])
                    removed.add(snd[i])
                    diffI = i
                    break 
            

            
            # if first different at i -> we have an edge 
            if diffI != -1:
                adjList[fst[diffI]].add(snd[diffI])
            elif len(fst) > len(snd):
                return ""
                
        # top sort on the graph
        visited = set()
        explored = set()
        res = []
        print(adjList)
        def dfs(ch):
            
            visited.add(ch)
            for adj in adjList[ch]:

                if adj in visited:
                    return False 

                if adj not in explored:
                    if not dfs(adj):
                        return False
            
            visited.remove(ch)
            # mark as visited 
            explored.add(ch)
            res.append(ch)

            return True 
        

        if not charSet:
            return ""

        starters = (starters - removed)
        if not adjList:
            return "".join(charSet)
        
        if not starters:
            return ""
  
        print("run dfs")
        for starter in starters:        
            if not dfs(starter):
                return ""


        for ch in charSet - explored:
            res.append(ch)
        return "".join(res[::-1]) 
