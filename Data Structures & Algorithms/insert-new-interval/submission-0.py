class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval) 
        intervals.sort(key = lambda x: x[0]) 


        output = [intervals[0]]

        for curStart, curEnd in intervals[1:]: 
            lastEnd = output[-1][1]
            if curStart <= lastEnd: 
                output[-1][1] = max(lastEnd, curEnd)
            else: 
                output.append([curStart, curEnd])

        return output