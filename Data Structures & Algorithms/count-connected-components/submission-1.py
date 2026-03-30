class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        ranks = [0]*n

        def find(i: int):
            parent = parents[i]

            if parent != parents[parent]:
                parents[parent] = find(parent)
                return parents[parent]
            
            return parent
        
        def unite(i: int, j: int) -> bool:
            irep = find(i)
            jrep = find(j)

            if irep == jrep:
                return False
            
            if ranks[irep] < ranks[jrep]:
                parents[irep] = jrep
            elif ranks[irep] > ranks[jrep]:
                parents[jrep] = irep
            else:
                parents[jrep] = irep
                ranks[irep] += 1
            
            return True
        res = n    
        for u, v in edges:
            if unite(u, v):
                res -= 1
        
        return res
