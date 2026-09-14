import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # So we want to find the minimum k which allows to eat all the bananas within h 
        # There's no reason for k to be greater than the max of piles[i] 
        # so we can have it start at that 
        # We can have a left and right pointer where left is 1 and the right is max of the piles 
        # then we have our middle pointer in the middle 
        # We then have hours count and if we exceed that, we need to increase the k
        # and if we undershoot, we can lower the k
        # and then 

        left = 1
        right = max(piles)
        
        k = float('inf')

        while left <= right: 
            middle = (right + left) // 2 
           
            hours = 0
            for i in range(len(piles)): 
                hours += math.ceil(piles[i] / middle)

            if hours > h: 
                left = middle + 1
            else: 
                right = middle - 1 
                k = min(k, middle)

        return k
