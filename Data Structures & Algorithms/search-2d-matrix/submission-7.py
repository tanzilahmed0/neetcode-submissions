class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Now let's do solution where we use binary search to find with row it's in, 
        # then another binary search to find the val 

        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0]) 

        top, bottom = 0, rows - 1 

        while top <= bottom: 
            mid = top + (bottom - top) // 2 
            if target < matrix[mid][0]: 
                bottom = mid - 1 
            elif target > matrix[mid][-1]: 
                top = mid + 1 
            else: 
                row = mid 
                break
        else: 
            return False
        
        left, right = 0, cols - 1
        while left <= right: 
            mid = left + (right - left) // 2
            if target == matrix[row][mid]: 
                return True
            elif target > matrix[row][mid]: 
                left = mid + 1 
            else: 
                right = mid - 1 

        return False            



        


        