class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # I think the approach is to sort the intervals based on the start point and then 
        # iterate through with a sliding window where it expands as long as it's overlapping where essentially 
        # the start value of the right is less than or equal to end value of left and then add that to new array 
        # you can initialize from output to store the most recent interval which is initialized as the first
        # interval 

        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]

        # Since we have the first interval, we can go ahead and skip it
        for start, end in intervals[1:]: 
            if start <= output[-1][1]: 
                output[-1][1] = max(end, output[-1][1]) 
            else: 
                output.append([start, end])
        
        return output

        
       