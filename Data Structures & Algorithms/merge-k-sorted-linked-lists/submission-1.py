# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i))
        
        head = None 
        cur = None 
        while heap:
            val, i = heapq.heappop(heap)
            
            if head == None:
                cur = head = lists[i]
            else:
                cur.next = lists[i]
                cur = lists[i]

            if lists[i].next != None:
                lists[i] = lists[i].next 
                heapq.heappush(heap, (lists[i].val, i))
        
        return head