class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        sortedkeys = sorted(counter.keys())


        for key in sortedkeys:
            val = counter[key]
            if val > 0:
                start = key

                # greedily take consecutive elements
                for num in range(start, start+groupSize):
                    
                    # not enough
                    if num not in counter or counter[num] < val:
                        return False 

                    counter[num] -= val
        
        return True