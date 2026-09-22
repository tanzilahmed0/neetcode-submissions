class Solution:
    def rob(self, nums: List[int]) -> int:

        # Recursively with memoization 
        # We can recursively go to each house and store how much money is at the next house we can visit 
        # So essentially at memo[i] we store the max of the 
        memo = {}
        def dfs(i): 
            if i >= len(nums): 
                return 0
            
            if i in memo:
                return memo[i] 
            
            memo[i] = max(dfs(i+2) + nums[i], dfs(i + 1)) 
            return memo[i] 
        
        return dfs(0)
            