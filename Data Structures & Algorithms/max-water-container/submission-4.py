class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Brute force approach, have a nested loop and calculate area by 
        # multiplying height by width and then making it the max area 
        # Or we can use two pointers
        maxArea = 0 

        l, r = 0, len(heights) - 1 
        while l < r: 
            width = r - l 
            height = min(heights[r], heights[l])
            area = height * width 
            maxArea = max(area, maxArea) 

            if heights[l] <= heights[r]: 
                l += 1 
            else: 
                r -= 1 
        
        return maxArea