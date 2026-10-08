class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # So essentially, we're trying to figure out if there's a subset that is equal to the target sum
        # which is half of the array 
        # At each index, we have the choice of either choosing to include it as part of our subset or not
        # 

        if sum(nums) % 2 != 0: 
            return False 
        
        half = sum(nums) // 2 
        n = len(nums)
        dp = [[None] * (half + 1) for _ in range(n+1)]

        for i in range(n + 1): 
            dp[i][half] = True 

        # so dp[i][currSum] represents if we've explored the current sum we have right now at this index, 
        # we can reach the target, so we'd check backwards 
        for i in range(len(nums) - 1, -1, -1): 
            # To represnet column
            for j in range(half): 
                # We skip the current number
                skip = dp[i+1][j]

                take = False 
                if j + nums[i] <= half: 
                    take = dp[i+1][j+nums[i]]
                
                dp[i][j] = skip or take 

        return dp[0][0]
