class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Use nums[:] to modify nums in place
        # First reverse string 
        # [5, 4, 3, 2, 1] becomes [1, 2, 3, 4, 5]
        nums[:] = nums[::-1] 

        # k = 2 
        # reverse subarray up to k
        # if k > len(nums)
        # 
        j = k % len(nums)
        nums[:j] = nums[:j][::-1]
        # reverse subarray from k to end
        nums[j:] = nums[j:][::-1]

    

        