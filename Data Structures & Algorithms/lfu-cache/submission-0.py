from collections import defaultdict, OrderedDict

class LinkedListNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right 

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0
    
    def append(self, node: LinkedListNode):
        if self.head == None:
            self.head = self.tail = node 
        else:
            self.tail.right = node
            node.left = self.tail
            self.tail = node 
        
        self.size += 1 
    
    def remove(self, node: LinkedListNode):

        if node == self.head:
            newHead = self.head.right 
            
            if newHead != None:
                newHead.left = None 
            
            if self.head == self.tail:
                self.head = self.tail = newHead
            else:
                self.head = newHead

        elif node == self.tail:
            prev = self.tail.left 

            prev.right = None 
            self.tail = prev 
        else:
            prev = node.left 
            nxt = node.right 

            prev.right = nxt
            nxt.left = prev 
        
        self.size -= 1


    def getSize(self):
        return self.size 


class LFUCache:

    def __init__(self, capacity: int):
        self.key2val = {}
        self.key2freq = defaultdict(int)
        self.freq2key = defaultdict(LinkedList) # use for breaking tie between highest freq keys
        self.key2node = {} # map key to ll node
        self.lowestFreq = 0
        self.capacity = capacity


    def counter(self, key: int) -> None:
        # for whenever a key got accessed

        # update frequency of key
        oldFreq = self.key2freq[key]
        newFreq = oldFreq + 1
        self.key2freq[key] = newFreq 
        
        # move node of key from old frequency ll to new freq ll 
        node = self.key2node[key]
        self.freq2key[oldFreq].remove(node)
        self.freq2key[newFreq].append(node)

        # if old freq is empty -> update lowest freq 
        if self.freq2key[oldFreq].size == 0:
            self.freq2key.pop(oldFreq)

            if self.lowestFreq == oldFreq:
                self.lowestFreq += 1
        


    def get(self, key: int) -> int:
        print("get", key)
        
        if key not in self.key2val:
            return -1 
        
        self.counter(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        print("call put, ", key, value)
        if key in self.key2val:
            self.counter(key)
            self.key2val[key] = value
        else:
            # check if capacity is exceeded 
            if len(self.key2val) == self.capacity:
                # if so, removed lru node from least frequent used node
                ll = self.freq2key[self.lowestFreq]
                head = ll.head
                ll.remove(ll.head)

                self.key2val.pop(head.key)
                self.key2freq.pop(head.key)
                self.key2node.pop(head.key)

                # no more key left for this lowest frequency
                if ll.size == 0:
                    self.freq2key.pop(self.lowestFreq)
                    
            
            # insert
            self.key2val[key] = value 
            self.key2freq[key] = 1
            self.key2node[key] = LinkedListNode(key=key)
            self.freq2key[1].append(self.key2node[key])
            self.lowestFreq = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)