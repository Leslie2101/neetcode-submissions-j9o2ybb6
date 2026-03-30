class MinStack:

    def __init__(self):
        self.prefixMins = deque()
        self.stack = deque()
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.prefixMins: 
            self.prefixMins.append(min(val, self.prefixMins[-1]))
        else:
            self.prefixMins.append(val)

    def pop(self) -> None:
        self.prefixMins.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefixMins[-1]
        
