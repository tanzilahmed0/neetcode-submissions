class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # We can use a slow and fast pointer 
        # The fast pointer moves while it's not equal to val 

        slow = 0 

        for fast in range(len(nums)): 
            if nums[fast] != val: 
                nums[slow] = nums[fast]
                slow += 1 
        #=
        return slow 
