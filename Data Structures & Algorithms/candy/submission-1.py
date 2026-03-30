class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        heap = []

        for i in range(n):
            heapq.heappush(heap, (ratings[i], i))
        
        candies = [1]*n

        while heap:
            rating, idx = heapq.heappop(heap)

            # check if the candy for this idx is enough? bonus if not enough
            if idx - 1 >= 0 and ratings[idx-1] < ratings[idx]:
                candies[idx] = max(candies[idx], candies[idx-1] + 1) 
            
            if idx + 1 < n and ratings[idx+1] < ratings[idx]:
                candies[idx] = max(candies[idx], candies[idx+1] + 1)
        print(candies)
        return sum(candies)

        