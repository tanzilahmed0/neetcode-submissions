class MinStack:
    # so I'm thinking we can simply implement current operations of the stack 
    # and then when initializing the minStack object, we init a minValue that starts at 
    # positive infinity. And then whenever getMin is called we return that value. 
    # but what if the popped value is the current min, we need to update it then

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.minVal = min(val, self.minVal)
        self.stack.append((val, self.minVal))
 
    def pop(self) -> None:
        self.stack.pop()
        if self.stack: 
            self.minVal = self.stack[-1][1]
        else: 
            self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
    # [-2] -> [-2, 0] -> [-2, 0, -3] -> return -3 -> [-2, 0] -> return 0, return -2 
    # -> [-2, 0, 2] -> [-2, 0, 2, -4] -> [-2, 0, 2, -4, 3] -> return -4 -> [-2, 0, 2, -4]
    # -> return -4 ->[-2, 0, 2] -> return -2 -> [-2, 0] -> return 0, return -2, [-2], 
