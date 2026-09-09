class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count = 0
        intervals.sort(key = lambda x: x[0])    
        prevEnd = intervals[0][1] 

        for curStart, curEnd in intervals[1:]: 
            if curStart >= prevEnd: 
                prevEnd = curEnd
            else: 
                # We don't actually have to delete the interval, so we can update 
                # the prevEnd to the smaller endpoint
                count += 1
                prevEnd = min(prevEnd, curEnd)
        
        return count
                 