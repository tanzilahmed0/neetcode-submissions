class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # We can use a stack for this problem 
        # We can push on to the stack until we run into an operator 
        # then we pop the top 2 elements on stack and do the operation
        # then we push the result on to the stack

        stack = []
        result = None

        operators = {'+', '-', '*', '/'}

        for i in tokens: 
            if i not in operators: 
                stack.append(int(i))
            else: 
                operand1 = stack.pop() 
                operand2 = stack.pop()
                print(operand1) 
                if i == '+': 
                    result = operand1 + operand2 
                    stack.append(result) 
                elif i == '-': 
                    result = operand2 - operand1
                    stack.append(result)
                elif i == '*': 
                    result = operand1 * operand2 
                    stack.append(result)
                elif i == '/': 
                    result = int(operand2 / operand1)
                    stack.append(result)
        
        return stack[-1]



        