class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # So a brute force approach would be to just have 2 nested loops 
        # and the nested loop would iterate until it finds a warmer temperature 
        # and then we'd update the result array at that index 

        # I think since we're looking at the history of the days i.e. how long till a warmer day, 
        # we can use something like a stack maybe 
        # we can iterate through temperatures and check to see if the current temp is warmer than the top of the 
        # stack. We can pop the top of the stack as long as the current temp is warmer 
        # So essentially the stack will have the days that we have not seen a warmer temperature for yet 

        stack = [] 
        result = [0] * len(temperatures) 

        for i, temp in enumerate(temperatures): 
            while stack and stack[-1][1] < temp: 
                result[stack[-1][0]] = i - stack[-1][0] 
                stack.pop()
            stack.append((i, temp))

        return result

        