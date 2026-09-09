class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we can use a variable to store the max amount of water
        # We use two pointers, and we calculate the area by multiplying 
        # the min height of the left and right pointer by the difference in indices
        # then we return maxArea 

        maxArea = 0 
        left, right = 0, len(heights) - 1 

        while left < right: 
            height = min(heights[left], heights[right])
            area = (right - left) * height 
            print(area)
            maxArea = max(area, maxArea)
            

            if heights[left] < heights[right]: 
                left += 1 
            else: 
                right -= 1

        return maxArea
        