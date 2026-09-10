class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '[': ']', '{': '}'}

        # We can add to the stack as long as characters are in the keys of parentheses
        # once we run into a closing bracket, we pop from the stack and see if it matches
        # opening bracket
        stack = []
        for char in s: 
            if char in parentheses.keys(): 
                stack.append(char)
            elif stack: 
                value = stack.pop()
                if parentheses[value] != char: 
                    return False 
            else: 
                return False
            
        if not stack: 
            return True
        else: 
            return False