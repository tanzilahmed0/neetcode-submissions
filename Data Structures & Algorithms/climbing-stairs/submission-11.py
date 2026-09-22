class Solution:
    def climbStairs(self, n: int) -> int:

        # so let's say im at step 0 to go to step 3 
        # I can either take 1 step then im at step 1, then I can take 1 step again, or 2 steps which i;d complete
        # or i can take 2 steps then im at step 2, then I'm basically at step 0 trying to get to 
        # step 1 so i only take one step 
        # So essentially i calculate the distinct ways to get to step 1, and then the distinct ways to get to step 2 
        # And the number of ways to get to step 3 is step 2 + step 1 
        # So essentially it's the sum of the previous steps 
        # So we can have a an empty array size n 
        # We recursively have the steps calculated by the previous 2 digits summed until we reach n and then 
        # we return last value of n 

        if n <= 2: 
            return n

        steps = [0] * n
        steps[0] = 1 
        steps[1] = 2
       

        for i in range(2, n): 
            steps[i] = steps[i-1] + steps[i-2]
  


        return steps[-1]

        