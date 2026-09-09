class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Since everything is sorted we can treat it as large 1d array 
        # Ok so we can set left to 0 and right to m*n-1 
        # the mid point is left + (right - left) // 2 
        # we then map the midpoint to it's 2d coordinate by row = mid // n, col = mid % n
        # then we compare and move pointers

        m = len(matrix)
        n = len(matrix[0])
        

        left = 0 
        right = m * n - 1
        
        while left <= right: 
            mid_point = left + (right - left) // 2 
            mid_row, mid_col = mid_point // n, mid_point % n

            if target == matrix[mid_row][mid_col]: 
                return True
            elif target > matrix[mid_row][mid_col]:
                left = mid_point + 1 
            elif target < matrix[mid_row][mid_col]:
                right = mid_point - 1 
        
        return False

        
                
        
        return False

