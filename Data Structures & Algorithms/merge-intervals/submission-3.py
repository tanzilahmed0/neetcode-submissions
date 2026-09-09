class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # what we can do is sort the intervals by starting point. 
        # Then we can go through the intervals one by one and check if the starting
        # point is less than or equal than the previous interval's end 
        # then we make that interval's end point the of the current and previous one 
        
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for curStart, curEnd in intervals:
            lastEnd = output[-1][1] 
            if curStart <= lastEnd: 
                output[-1][1] = max(curEnd, lastEnd)
            else: 
                output.append([curStart, curEnd])

        return output



        