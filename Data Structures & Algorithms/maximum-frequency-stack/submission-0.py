from collections import defaultdict, OrderedDict
class FreqStack:

    def __init__(self):
        self.item2freq = defaultdict(int)
        self.freq2item = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.item2freq[val] += 1
        self.freq2item[self.item2freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.item2freq[val])

    def pop(self) -> int:
        val = self.freq2item[self.maxFreq].pop()
        self.item2freq[val] -= 1

        if not self.freq2item[self.maxFreq]:
            self.freq2item.pop(self.maxFreq)
            self.maxFreq -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()