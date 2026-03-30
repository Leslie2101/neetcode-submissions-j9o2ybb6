class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        visited = set()
        a,b,c = target
        for triplet in triplets:
            curValid = set()
            for i in range(3):
                if target[i] == triplet[i]:
                    curValid.add(i)
                elif target[i] < triplet[i]:
                    curValid = set()
                    break
            
            if not curValid:
                continue

            visited |= curValid
        
        return len(visited) == 3 
            
