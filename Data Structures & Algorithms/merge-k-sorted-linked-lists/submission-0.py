# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, (node.val, i))
        
        head = None
        tail = None 
        # insert each smallest element to list
        while heap:
            val, i = heapq.heappop(heap)
            

            if head == None:
                head = tail = lists[i]
            else:
                tail.next = lists[i]
                tail = tail.next

            lists[i] = lists[i].next
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))
            
        return head
