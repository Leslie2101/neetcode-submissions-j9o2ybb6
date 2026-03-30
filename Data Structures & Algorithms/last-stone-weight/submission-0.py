class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            fst, snd = heapq.heappop(stones), heapq.heappop(stones)

            if fst < snd:
                heapq.heappush(stones, fst - snd)
        
        return -stones[0] if stones else 0
            


        