class MedianFinder:

    def __init__(self):

        self.lowers = [] # max heap
        self.biggers = [] # min heap
        self.size = 0 # for calculating median 
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowers, -num)

        # make sure biggers >= lowers by at most 1
        if len(self.lowers) - len(self.biggers) == 1:
            heapq.heappush(self.biggers, -heapq.heappop(self.lowers))

        # make sure the order is correct
        while self.lowers and self.biggers and -self.lowers[0] > self.biggers[0]:
            # swap 
            lowTop = -heapq.heappop(self.lowers)
            highBot = heapq.heappop(self.biggers)

            heapq.heappush(self.lowers, -highBot)
            heapq.heappush(self.biggers, lowTop)

        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.lowers[0] + self.biggers[0])/2
        
        return self.biggers[0]

        
        