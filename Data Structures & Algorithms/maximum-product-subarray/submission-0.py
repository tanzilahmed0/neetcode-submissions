class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # How do we handle multiplying negatives
        # So i guess what we could do is starting from each index get a contiguous product
        # so in dp[i] we store the current product

        # So essentially at each index, we store the previous maxProduct and the previous minProduct
        # So we have 3 potential products, 

        # [2, 4, -3, 5]
        # [[2,2], [8, 4], [-3, -24], [5, -120]]

        dp = [] 
        dp.append([nums[0], nums[0]])

        for i in range(1, len(nums)): 
            minProduct = nums[i] * dp[i-1][0]
            maxProduct = nums[i] * dp[i-1][1]

            dp.append([max(minProduct, maxProduct, nums[i]), min(minProduct, maxProduct, nums[i])])

        result = float('-inf')

        for product in dp: 
            result = max(product[0], result)

        return result
        