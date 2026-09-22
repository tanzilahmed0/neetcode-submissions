class Solution:
    def rob(self, nums: List[int]) -> int:       

        # So at each house i can choose to rob it or not 
        # We can kind of do this with a bottom up dynamic programming approach 
        # [2, 9, 8, 3, 6] 
        # I think you can maybe do 2 passes to fill up dp
        # So 1 pass fills up including the last element and excluding first element 
        # and 2nd pass fills up vice versa 

        n = len(nums) 
        if not nums: 
            return 0 
        
        if n <= 2: 
            return max(nums)

        dp1 = [0] * (n - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        # First pass: 
        for i in range(2, n-1): 
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])       

        dp2 = [0] * (n - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2]) 
        # Second pass: 
        for i in range(3, n): 
            dp2[i-1] = max(dp2[i-3] + nums[i], dp2[i-2])
     
        return max(dp1[-1], dp2[-1])
        
      