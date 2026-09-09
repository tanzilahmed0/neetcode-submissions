class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opened = ['(', '[', '{']
        closed = [ ')', ']', '}']

        for char in s: 
            if char in opened: 
                stack.append(char) 
            elif stack and opened.index(stack[-1]) == closed.index(char):
                stack.pop()
            else: return False 
        
        if len(stack) == 0: 
            return True
        else: return False
                
            

                

