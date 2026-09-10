class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # So we keep going through tokens until see an operand. 
        # and then we perform the operation on the last 2 elements 
        # we can use a stack that pushes if it's an integer 
        # and then when it encounters an operand, we pop the last 2 elements 
        # and then perform that operation and add it back to the stack 

        operators = {'+', '-', '*', '/'}
        stack = []
        for i in tokens: 
            if i not in operators: 
                stack.append(int(i))
            else: 
                val1 = stack.pop()
                val2 = stack.pop()
                
                if i == '+': 
                    stack.append(val1 + val2) 
                elif i == '-': 
                    stack.append(val2 - val1) 
                elif i == '*': 
                    stack.append(val1 * val2) 
                elif i == '/': 
                    stack.append(int(val2 / val1))
        
        return stack[-1]