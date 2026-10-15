class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # The product can always increase if it's positive 
        # but if we have a negative, we can wait and see if there's another negative 
        # When we run into a negative number, we can store that as a preivous product 
        # and when we move on to the next digit, we reset the product again but also have 
        # previous product that we can use if we run into another negative number 
        # 
        # We initialize dp where dp[i] has the min and max product ending at index i
        # We iterate through the rest of nums, we calculate the maximum and min product ending at nums[i]
        # dp = [(2, 2), (4, 8), (-24, -3), (-96, 5)]
        # dp = [(-3, -3), (0, 0), (-2, 0)]
        dp = [] 
        dp.append((nums[0], nums[0]))
        result = nums[0]

        for i in range(1, len(nums)): 
            minProduct = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            maxProduct = max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            result = max(minProduct, maxProduct, result)
            dp.append((minProduct, maxProduct))

        return result


   
            


            
            
