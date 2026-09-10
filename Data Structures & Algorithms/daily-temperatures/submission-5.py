class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # Brute force, we can iterate through temperatures with i and j, 
    # i is at current temp, then j scans until it reaches a larger temperature 
    # and then we store j - i in result[i]
    # 
    # Or at each element, we check the top of the stack to see if it's less than the current val 
    # if it is then pop it, we store the temp and index in the stack and then subtract the current index with the index of what we're popping and store that in results 


        result = [0] * len(temperatures)
        stack = []
    
        # [89]
        for idx, temp in enumerate(temperatures):  
            while stack and temp > stack[-1][1]:
                top_idx, top_temp = stack.pop()
                result[top_idx] = idx - top_idx

            stack.append((idx, temp))

        return result 

