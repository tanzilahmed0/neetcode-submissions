class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # we need to figure out the pivot index, becuase then on each side, the array 
        # is sorted. So what we can do is do a binary search and check if the right pointer 
        # is less than the middle. If is, then we can move the left pointer because we know that pivot index is
        # some where there 
        # If not, the pivot has to be towards the left so we make right = mid bc the pviot could be mid itself 

        left, right = 0, len(nums) - 1 

        while left < right: 
            mid = (left + right) // 2 
            if nums[right] < nums[mid]: 
                left = mid + 1 
            else: 
                right = mid 

        pivot = left
        if pivot == 0: 
            new_left = 0 
            new_right = len(nums) -1
        elif nums[0] <= target <= nums[pivot-1]: 
            new_left = 0
            new_right = pivot-1
        elif nums[pivot] <= target <= nums[-1]: 
            new_left = pivot
            new_right = len(nums) - 1 
        else: 
            return -1 
        
        while new_left <= new_right: 
            middle = (new_left + new_right) // 2 
            if target > nums[middle]: 
                new_left = middle + 1 
            elif target < nums[middle]: 
                new_right = middle - 1 
            else: 
                return middle

        return -1

            