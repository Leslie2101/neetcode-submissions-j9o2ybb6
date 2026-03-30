
class LinkedListNode:
    def __init__(self, key=None, prev=None, nxt=None):
        self.key = key
        self.prev = prev
        self.nxt = nxt 


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0 
    
    def append(self, node: LinkedListNode) -> None:
        if self.head == None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.nxt = node
            self.tail = node 
        
        self.size += 1
    
    def remove(self, node: LinkedListNode) -> None:
        
        if self.head == node:
            self.head = self.head.nxt 

        elif self.tail == node:
            prev = self.tail.prev 
            prev.nxt = None 
            self.tail = prev

        else:
            prev = node.prev 
            nxt = node.nxt 
            prev.nxt = nxt
            nxt.prev = prev 




class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyValueMap = {} # map key - value 
        self.keyNodeMap = {} # map key - linkedlist node 
        self.linkedlist = LinkedList()

    def get(self, key: int) -> int:
        # key, value pair -> map / dictionary

        if key not in self.keyValueMap:
            return -1
        
        # if it is -> make sure key is something just recently used
        node = self.keyNodeMap[key]
        self.linkedlist.remove(node)
        self.linkedlist.append(node)
        return self.keyValueMap[key]

    def put(self, key: int, value: int) -> None:
        

        if key in self.keyValueMap:
            self.keyValueMap[key] = value
            node = self.keyNodeMap[key]
            self.linkedlist.remove(node)
            self.linkedlist.append(node)
        else:
            node = LinkedListNode(key=key)
            self.linkedlist.append(node)

            self.keyNodeMap[key] = node
            self.keyValueMap[key] = value

        
            # check exceeding capacity
            if len(self.keyValueMap) > self.capacity:
                # remove LRU node 
                node = self.linkedlist.head
                self.linkedlist.remove(node)

                self.keyValueMap.pop(node.key)
                self.keyNodeMap.pop(node.key)




        
