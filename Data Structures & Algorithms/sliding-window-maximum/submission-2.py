class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        # fill in first k element 
        for i in range(k):
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
                

        # fill in result using decreasing queue
        # head: biggest num, tail: smaller num in the window
        res = [nums[queue[0]]]


        for i in range(k, len(nums)):
            # maintain monotonic
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            # add current number to tail
            queue.append(i)

            # check current window size 
            if queue[-1] - queue[0] + 1 > k:
                queue.popleft()
            
            res.append(nums[queue[0]])
        
        return res


            

