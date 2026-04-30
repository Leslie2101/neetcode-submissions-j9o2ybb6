class StockSpanner:

    def __init__(self):
        # monotonic stack 
        self.stack = deque() # (val, idx) where the top is the smallest value
        self.idx = 0

    def next(self, price: int) -> int:
        # keep increasing stack 

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop() 
        

        self.stack.append((price, self.idx))
        self.idx += 1

        print(self.stack)

        # return val difference between the 2 top idx
        if len(self.stack) == 1:
            return self.stack[-1][1] + 1 
        
        return self.stack[-1][1] - self.stack[-2][1] 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)