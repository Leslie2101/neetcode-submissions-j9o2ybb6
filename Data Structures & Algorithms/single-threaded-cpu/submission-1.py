class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks = ((enqueueTime, processingTime, index) for index, (enqueueTime, processingTime) in enumerate(tasks))
        queue = deque(sorted(range(len(tasks)), key=lambda x: (tasks[x][0], tasks[x][1], x)))

        availables = []
        res = []

        t = 1
        while queue or availables:
            # find all available tasks from queue using enqueue time 
            while queue and tasks[queue[0]][0] <= t:
                idx = queue.popleft()
                enqueueTime, processingTime = tasks[idx] 
                heapq.heappush(availables, (processingTime, idx))
            
            

            # from available tasks, choose one with shortest time - smallest index 
            # ... update time for processing that task
            if availables:
                processTime, idx = heapq.heappop(availables)
                res.append(idx)
                t += processTime 
            else:
                # time skip to next available time 
                t = tasks[queue[0]][0]
        
        return res
        