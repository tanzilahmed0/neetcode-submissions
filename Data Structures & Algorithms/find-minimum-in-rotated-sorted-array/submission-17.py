class Solution:
    def findMin(self, nums: List[int]) -> int:
        # To do binary search, the input must already be sorted 
        # We can do a binary search to find where the rotation point is 
        if not nums: 
            return

        left, right = 0, len(nums) - 1 

        while left < right: 
        
            mid = left + (right - left) // 2 
           

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]: 
                # since the minimum could be mid itself, we shouldn't exclude it 
                right = mid 
        

        return nums[left]
            

        

                
            
        