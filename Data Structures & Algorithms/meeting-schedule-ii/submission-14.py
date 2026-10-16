import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # [[1, 5], [2, 6], [7, 10], [8, 12]]
        # We can use a min heap to store meeting end times 
        # When a meeting overlaps, we increment count by one 
        # and then when it doesn't overlap we pop from min heap and then decrement the count 
        # and push the current end time to the interval 
        # We check if the end time is greater than the end time of the root of heap each time 

        # count = 2
   
        rooms = 1 
        if not intervals:
             return 0
        n = len(intervals) 
  
        intervals.sort(key = lambda x:x.start)
        
        heap = []
        heapq.heappush(heap, intervals[0].end)
        count = 1 
        for i in range(1, n): 
            if intervals[i].start >= heap[0]: 
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)

        return len(heap)