class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # If it's rotated n times, it's the original array 
        # We want to locate where there's a pivot in the array 
        # Basically where is the rotation point? 
        # The rotation point is where nums[i-1] > nums[i] < nums[i+1]
        # Because that means the right side of the pivot is sorted 
        # and the left side of the pivot is sorted 
        # and then we can do a binary search on the side of the array 
        # that the target is potentially in 
        # We do a binary search to find the pivot first 
        # If the middle is greater than left index, the pivot can't be on that side 
        # because it means it's sorted 
        # Then we move left to middle 
        # if middle is less then right index, it's on the other side 
        # if middle is > left and less than right, we've found the pivot 
        # after that we do a binary search by comparing if target is < left 
        # meaning it's on that side and vice versa for right side
        # [3, 1, 2]
        #. l. r
        # [2, 3, 0, 1]
        left, right = 0, len(nums) - 1 
        pivot = 0 
        if nums[left] > nums[right]: 
            while left < right: 
                middle = (left + right) // 2 
                if nums[right] <= nums[middle]: 
                    left = middle + 1 
                else: 
                    right = middle 
            pivot = right

        if target == nums[pivot]: 
            return pivot 
        elif pivot != 0 and nums[0] <= target <=  nums[pivot-1]: 
            left, right = 0, pivot-1
        elif pivot != 0 and nums[pivot] <= target <= nums[-1]: 
            left, right = pivot, len(nums) - 1 
        else: 
            left, right = 0, len(nums) - 1 


        while left <= right: 
            middle = (left + right) // 2 
            if target == nums[middle]: 
                return middle
            elif target > nums[middle]: 
                left = middle + 1 
            else: 
                right = middle - 1 
        return -1
  
    
            
            

