from collections import defaultdict
import math
class DSU:
    # DSU 
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0]*n

    def find(self, i):
        parent = self.parents[i]

        if parent != self.parents[parent]:
            self.parents[parent] = self.find(parent)
            return self.parents[parent]
        
        return parent 
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)

        if irep == jrep:
            return False 
        
        if self.ranks[irep] > self.ranks[jrep]:
            self.parents[jrep] = irep 
        elif self.ranks[irep] < self.ranks[jrep]:
            self.parents[irep] = jrep 
        else:
            self.parents[jrep] = irep 
            self.ranks[irep] += 1
        
        return True 

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # pseudo edges: edge can be swapped with each other for MST
        # critical edges: edge must be in MST 


        edgesGroup = defaultdict(list)
        edgeIndices = sorted(range(len(edges)), key=lambda x: edges[x][2])
        criticals = []
        pseudos = []

        def calculateMST(indices, removedIdx, forced):
            dsu = DSU(n=n)
            i = 0
            mst = 0
            cnt = 0

            if forced != -1:
                a, b, w = edges[forced]
                dsu.unite(a, b)
                mst += w
                cnt += 1


            while i < len(indices) and cnt < n-1:
                idx = indices[i]
                if idx == removedIdx or idx == forced:
                    i += 1
                    continue
                
                a, b, w = edges[idx]
                if dsu.unite(a, b):
                    mst += w 
                    cnt += 1
                
                i += 1
            
            if cnt < n-1:
                return math.inf
            return mst 

        actualMST = calculateMST(edgeIndices, -1, -1)
        print(actualMST)
        for i in range(len(edges)):
            # exclude edge i from mst 
            calculatedMST = calculateMST(edgeIndices, i, -1)
            if calculatedMST > actualMST:
                criticals.append(i)
            else:
                calculated = calculateMST(edgeIndices, -1, i)

                print(i, edges[i], calculated)
                if calculated == actualMST:
                    pseudos.append(i)
            

        return [criticals, pseudos]



        
        




