import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # When does 2 cars become a car fleet? 
        # We can subtract the starting position and then divide it by speed 
        # We can start the number of car fleets as the length of the array 
        # And we can calculate the hours and we decrement the number of fleets every time
        # it matches hour we've seen before 
        # This only catches fleets that meet at the target
        
        cars = list(zip(position, speed))
        cars.sort()
        stack = []
     
        for i in range(len(cars)):
            # Since we're processing farthest to closest car, 
            # if the hours of the current car it takes to reach the destination is greater than 
            # the top of the stacks, we can pop the top and decrement fleets. if that car that 
            # is now on the top of stack will also reach the same pos as future car, it doesnt' matter 
            # because now it's considered one fleet, we'd just return the length of the stack at the end
            hours = (target - cars[i][0]) / cars[i][1] 
            while stack and stack[-1][2] <= hours: 
                stack.pop()
            stack.append((cars[i][0], cars[i][1], hours))

        return len(stack)

            # 1, 2, 4.5
            # 0, 3, 3.333 



        




        
