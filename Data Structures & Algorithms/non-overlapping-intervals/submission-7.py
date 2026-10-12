class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,10],[2,3],[4,5],[6,7]]
        # [[1,4],[2,5],[3,6],[4,7]]
        # [[1,5],[2,3],[3,4]]
        # [[1, 4], [3, 5], [4, 6]]

        intervals.sort(key=lambda x: x[0])
        kept = [intervals[0]]

        for i in range(1, len(intervals)): 
            if intervals[i][0] < kept[-1][1]:
                if intervals[i][1] < kept[-1][1]: 
                    kept[-1] = intervals[i]
            else: 
                kept.append(intervals[i])
        
        return len(intervals) - len(kept)

                    


