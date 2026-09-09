class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # For it to be a valid container, one side can't be less than the other
        max_area = 0 
        left = 0
        right = len(heights) - 1


        while left < right: 
            if heights[left] < heights[right]: 
                area = (right-left) * heights[left]
                if area > max_area: 
                    max_area = area
                left += 1
            elif heights[left] >= heights[right]:
                area = (right-left) * heights[right]
                if area > max_area:
                    max_area = area
                right -= 1 
        
        return max_area
        