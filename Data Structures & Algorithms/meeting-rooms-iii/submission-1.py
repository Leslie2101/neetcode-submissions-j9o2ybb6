class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        waitings = []
        availables = []


        for i in range(n):
            availables.append(i) # available time, room 


        
        meetings.sort()
        freq = [0]*n

        for meeting in meetings:
            # print(f"{meeting=}")
            duration = meeting[1] - meeting[0]

            # print(f"{waitings=}")
            
            # load available rooms 
            while waitings and waitings[0][0] <= meeting[0]:
                t, i = heapq.heappop(waitings)
                heapq.heappush(availables, i)

            # print(f"{availables=}")

            # get room 
            if availables:
                i = heapq.heappop(availables)
                # print("pick room", i)
                freq[i] += 1

                meeting_time = meeting[0]
                

                # update that room next available time 
                heapq.heappush(waitings, (meeting_time + duration, i))
            else:
                meeting_time, i = heapq.heappop(waitings)
                # print(f"{i=}")
                freq[i] += 1
                # update that room next available time 
                heapq.heappush(waitings, (meeting_time + duration, i))

        # print(freq)
        # check room with highest used 
        highestUsed = max(freq)

        for i in range(n):
            if freq[i] == highestUsed:
                return i
        
        return 0
        
