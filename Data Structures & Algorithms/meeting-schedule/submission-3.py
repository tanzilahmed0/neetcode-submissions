"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # We can just iterate through the intervals, and see if there's an overlap
        # If there is we return false 
        # Basically we can sort by the start time and then we iterate from the 2nd index, 
        # if the start time of that is less than the end time of the previous 
        # we have a conflict 
        intervals.sort(key = lambda x: x.start)
        n = len(intervals) 
        for i in range(1, n): 
            if intervals[i].start < intervals[i-1].end:
                return False 
        
        return True 
            

