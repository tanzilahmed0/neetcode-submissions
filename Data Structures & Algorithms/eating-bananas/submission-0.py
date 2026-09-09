import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        print(sum(piles))

        # for piles it takes Koko ceil(piles[i] / k) to finish eating the piles
        # k has to be <= max pile, there is no reason to ever eat faster than that
        # left pointer can just be 1, slowest speed Koko can eat at 
        # Since h is always >= than the length of piles, the max amount of time you can 
        # take is >= h
        # so we have to check if the sum of (ceiling(piles[i] / k) <= h
        # because we have to finish 1 pile before moving on to the next 

        left, right = 1, max(piles)
        result = 1


        while left <= right: 
            mid = left + (right - left) // 2 
            sums = 0
            for i in piles: 
                sums += (math.ceil(i / mid))
                
            if sums <= h: 
                result = mid
                right = mid - 1 
            else: 
                left = mid + 1 

        
        return result


        