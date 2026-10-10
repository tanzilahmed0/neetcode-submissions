class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort(key=lambda x:x[0])
        
        # We sort our intervals by the start point 
        # If the start of hte current interval is <= end of the last interval we can merge them 
        # to avoid indexing out of bounds we can start from index 1 
        # To consider consecutive elemnts we can init result

        result = [intervals[0]]

        for i in range(1, len(intervals)): 
            start, end = intervals[i][0], intervals[i][1]
            if start <= result[-1][1]:
                result[-1][1] = max(end, result[-1][1])
            else: 
                result.append([start, end])
        
        return result