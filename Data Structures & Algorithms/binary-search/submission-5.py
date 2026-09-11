class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) -1

        def binarySearch(target, nums, start, end): 
            middle = (start + end) // 2

            if start > end: 
                return -1
            
            if nums[middle] == target: 
                return middle 
            elif nums[middle] > target: 
                return binarySearch(target, nums, start, middle-1) 
            else: 
                return binarySearch(target, nums, middle+1, end)

        return binarySearch(target, nums, start, end)