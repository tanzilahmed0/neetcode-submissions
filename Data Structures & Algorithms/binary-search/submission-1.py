class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array has to be sorted for binary search 
        # we check if target is < or > than nums[mid]
        # if it's less than, we move right pointer to just before mid point
        # if it's greater than, we move left pointer to just after mid point 
        # we continue until left and right pointers meet 

        mid = (len(nums) // 2)
        left = 0 
        right = len(nums) - 1 

        while left <= right: 
            if target < nums[mid]: 
                right = mid - 1 
                mid = left + (right - left) // 2
            elif target > nums[mid]: 
                left = mid + 1 
                mid = left + (right - left) // 2
            else: 
                return mid 

        return -1
        