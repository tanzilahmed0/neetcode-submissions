class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Since it's sorted but rotated, at some point there will be the rotating point (pivot)
        # We can use a binary search to find that pivot 
        # So for example we check if nums[left] > nums[mid] < nums[right], because if it is, that means 
        # that part is sorted and there is no pivot 
        # but if nums[mid] > nums[right] or nums[mid] < nums[left], that means there's a pivot point somewhere in that range, and the pviot index is the minimum in the array 
        # we can do binary search on each half of the array to find the pivot point 

        left, right = 0, len(nums) - 1 

        while left < right: 
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1 
            else:
                right = mid
        
        return nums[right]
        
     
