class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # what we can do is sort the intervals by starting point. 
        # Then we can go through the intervals one by one and check if the starting
        # point is less than or equal than the previous interval's end 
        # then we make that interval's end point the of the current and previous one 
        
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)): 
            prevEnd = output[-1][1] 
            if intervals[i][0] <= prevEnd: 
                output[-1][1] = max(prevEnd, intervals[i][1])
            else: 
                output.append(intervals[i])


        return output


        