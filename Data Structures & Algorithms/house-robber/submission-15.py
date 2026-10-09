class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # At each house, we can either rob it or not rob it
        # If we rob it, we have to move forward 2 spots
        # if we don't rob it we can move forward one house 
        # So for brute force, we can recursively try every combination of houses we can rob 
        # given the constraints and then return the maximum 

        # dfs(i) is the maximum amount of money i can rob from this current index
        memo = {}
        def dfs(i): 
            if i in memo: 
                return memo[i]
            if i >= len(nums): 
                return 0
            
            # we rob it 
            rob = dfs(i + 2) + nums[i] 

            # skipping it 
            skip = dfs(i + 1) 
            memo[i] = max(rob, skip)
            return memo[i]
    
        return dfs(0)