class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # what is the max value of k so that we finish all the bananas 
        # in h hours? The max value of k is the height of tallest pile
        # because she'll finish the biggest pile in 1 hours and all the other ones
        # in less than 1 hour (equaling to 1 hour) so 1 <= k <= max(piles)
        # We can treat this as sorted, and run a binary search for k
        # We can sum up piles[i] // k rounded up and see if it's less than h
        # if it is it's valid. 
        # FORMULA FOR INTEGER DIVISION AND ROUND UP: P/K = (P + K-1) // K

        min_k = 1 
        left, right = 1, max(piles)

        while left <= right: 
            mid = left + (right - left) // 2 
            total_hours = 0
            for i in piles: 
                # We calculate the hours it takes for each pile and sum it up
                hour = (i + mid -1) // mid
                total_hours += hour
            if total_hours > h: 
                left = mid + 1 
            elif total_hours <= h: 
                min_k = mid
                right = mid-1

        return min_k

        