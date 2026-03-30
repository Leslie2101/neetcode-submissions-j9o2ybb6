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
        
        def unite(i: int, j: int):
            irep = find(i)
            jrep = find(j)

            if irep == jrep:
                return 
            
            if ranks[irep] < ranks[jrep]:
                parents[irep] = jrep
            elif ranks[irep] > ranks[jrep]:
                parents[jrep] = irep
            else:
                parents[jrep] = irep
                ranks[irep] += 1
        
        for u, v in edges:
            unite(u, v)
        
        groups = set()
        for i in range(n):
            groups.add(find(i))
        
        return len(groups)
