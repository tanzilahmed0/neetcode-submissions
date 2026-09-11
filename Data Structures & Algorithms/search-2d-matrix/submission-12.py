class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1

        row = 0

        while top <= bottom:
            mid = (bottom + top) // 2 
            if target > matrix[mid][-1]: 
                top = mid + 1 
            elif matrix[mid][0] <= target <= matrix[mid][-1]: 
                row = mid 
                break
            else: 
                bottom = mid - 1 
        
        left, right = 0, cols - 1 
        while left <= right: 
            middle = (left + right) // 2 

            if target > matrix[mid][middle]: 
                left = middle + 1 
            elif target < matrix[mid][middle]: 
                right = middle - 1 
            else: 
                return True 
        
        return False