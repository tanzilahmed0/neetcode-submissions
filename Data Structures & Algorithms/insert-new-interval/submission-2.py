class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        left, right = 0, len(intervals) - 1 
        target = newInterval[0]

        while left <= right: 
            middle = (left + right) // 2
            if intervals[middle][0] < target: 
                left = middle + 1
            else: 
                right = middle - 1

        intervals.insert(left, newInterval)

        result = []
        for interval in intervals: 
            if not result or result[-1][1] < interval[0]: 
                result.append(interval)
            else: 
                result[-1][1] = max(result[-1][1], interval[1])

        return result
