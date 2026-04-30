from sortedcontainers import SortedList
class MyCalendar:
    
    def __init__(self):
        self.lst = SortedList() # [start1, end1, start2, end2, ...]
        

    def book(self, startTime: int, endTime: int) -> bool:

        print(self.lst)

        # l = bisect right on start1 
        l = self.lst.bisect_right(startTime)

        # r = bisect left on endTime 
        r = self.lst.bisect_left(endTime)

        # insertable if (l, r) is both even
        print(startTime, endTime, l, r)
        if l % 2 or r % 2 or l!=r:
            return False 

        self.lst.add(startTime)
        self.lst.add(endTime)
        return True 


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)