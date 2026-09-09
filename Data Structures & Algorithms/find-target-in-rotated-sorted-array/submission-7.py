class Solution:
    def search(self, nums: List[int], target: int) -> int:             
        # So first we need to find side of the array is the 
        # search space for target, and we can do this using 
        # binary search 

        left, right = 0, len(nums) - 1 

        while left <= right: 
            mid = left + (right - left) // 2 

            if target == nums[mid]: 
                return mid 

            # We check if the left half of the array is sorted 
            elif nums[left] <= nums[mid]: 
                # if target is in the left half, we shrink search space to the left half
                if nums[left] <= target <= nums[mid]: 
                    right = mid - 1
                # otherwise, we go to the right half 
                else: 
                    left = mid + 1 

            # the right half is sorted, check if target is within that range, if it is
            # shrink search space to right half, other wise, go to left half 
            elif nums[mid] <= nums[right]: 
                if nums[mid] <= target <= nums[right]: 
                    left = mid + 1 
                else: 
                    right = mid - 1 
            
        return -1

        