class Solution:
    def isValid(self, s: str) -> bool:
        # store closing bracket because you encounter them later and 
        # need to match them with their matching opening bracket 
        brackets = {')' : '(', '}' : '{', ']' : '['} 

        stack = [] 

        for ch in s: 
            if ch in brackets.keys(): 
                if not stack or brackets[ch] != stack[-1]: 
                    return False 
                stack.pop()
            elif ch in brackets.values(): 
                stack.append(ch)

        
        if len(stack) == 0: 
            return True
        else: 
            return False

        