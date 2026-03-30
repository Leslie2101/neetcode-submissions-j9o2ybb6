from sortedcontainers import SortedList
import bisect
class TimeMap:

    def __init__(self):
        self.store = defaultdict(SortedList)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if not self.store[key]:
            return ""

        insertionPoint = self.store[key].bisect_right((timestamp, "z"*101))
        print(self.store[key], insertionPoint)
        return self.store[key][insertionPoint-1][1] if insertionPoint >= 1 else ""
        
