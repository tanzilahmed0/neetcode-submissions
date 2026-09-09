class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}

        stack = [] 

        if len(tokens) == 1: 
            return int(tokens[0])

        result = 0

        for i in tokens: 
            if i not in operators: 
                stack.append(int(i)) 
            else: 
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())

                print(operand2)

                if i == '+': 
                    result = operand2 + operand1
                elif i == '-': 
                    result = operand2 - operand1
                elif i == '*': 
                    result = operand2 * operand1 
                elif i == '/': 
                    result = int(operand2 / operand1)
                
                stack.append(result)

        return result
                