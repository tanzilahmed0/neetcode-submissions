class Solution:
    def isValid(self, s: str) -> bool:

        # Ok so since we have to start with an opening parentheses, we can 
        # keep going through the string until we reach a closing bracket. 
        # Once we reach a closing bracket, we check the top of the stack to see 
        # if it's valid opening bracket since it's the most recent one 
        # if it is, we pop it then continue 
        # If at the end the stack is empty, we know that we processed all the parentheses 
        # so we can return True 

        parentheses = {')': '(', ']': '[', '}': '{' }
        stack = []

        for char in s: 
            if char in parentheses.values(): 
                stack.append(char) 
            elif stack and stack[-1] == parentheses[char]: 
                stack.pop()
            else: 
                return False 
        
        return not stack
                
                
        