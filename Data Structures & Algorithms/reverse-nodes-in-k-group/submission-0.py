# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def reverseGroup(groupHead: ListNode, groupTail: ListNode) -> List[ListNode]:
            
            cur = groupHead
            prev = None 


            while cur != groupTail:
                print(cur.val)
                nxt = cur.next 
                cur.next = prev                 
                prev = cur
                cur = nxt
            
            # do for last item 
            nxt = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nxt
            
            return prev, groupHead


            

        
        prevHead = prevTail = None
        finalHead = None 


        curNode = head 
        curHead = None 
        curTail = None 
        count = 0

        while curNode != None:
            count += 1
            nxtNode = curNode.next 

            # update group 
            if curHead == None:
                curHead = curTail = curNode 
            else:
                curTail = curNode

            

            # check group size
            if count % k == 0:
                print("detect:", curHead.val, curTail.val)
                newHead, newTail = reverseGroup(curHead, curTail)
                print("made:", newHead.val, newTail.val)
                
                if prevTail != None:
                    prevTail.next = newHead
                elif finalHead == None:
                    finalHead = newHead 
            
                
                newTail.next = nxtNode
                
                prevHead = newHead
                prevTail = newTail
                curHead = curTail = None 


            curNode = nxtNode
        



        return finalHead


