class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist, point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        print(heap)
        return [item[1] for item in heap]


         