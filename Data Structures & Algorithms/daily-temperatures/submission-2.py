class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # We enumerate because we want the indices

        result = [0] * len(temperatures) 
        stack = []



        for i, temp in enumerate(temperatures): 
            if not stack: 
                stack.append(i) 
            while stack and temp > temperatures[stack[-1]] :  
                result[stack[-1]] = (i - stack[-1])
                stack.pop()
            stack.append(i)
        
        return result







        