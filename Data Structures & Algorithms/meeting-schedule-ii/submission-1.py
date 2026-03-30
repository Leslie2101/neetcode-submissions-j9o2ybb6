"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
    
        intervals.sort(key=lambda x: x.start)
        rooms = [] # containing non-overlapping schedule

        for interval in intervals:
            start, end = interval.start, interval.end
            # check if there is any available room for this
            foundRoom=False
            for i in range(len(rooms)):
                if rooms[i] <= start:
                    rooms[i] = max(rooms[i], end)
                    foundRoom = True
                    break 
            

            # if not, put the meeting into that room
            if not foundRoom:
                rooms.append(end)
        
        return len(rooms)


        