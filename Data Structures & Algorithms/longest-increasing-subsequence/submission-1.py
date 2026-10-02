class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
   
        # At each number we can choose to keep or discard that number 
        # If we pick that number, then all future numbers we pick have to be larger 
        # than that current number 

        memo = {}
        def dfs(i, prev): 
            if i == len(nums): 
                return 0 

            if (i, prev) in memo: 
                return memo[(i, prev)]
            
            skip = dfs(i+1, prev)
            take = 0
                      
            if nums[i] > prev:                
                take = 1 + dfs(i+1, nums[i])
            
            memo[(i, prev)] = max(skip, take)
            return memo[(i, prev)]
        
        return dfs(0, float('-inf'))



            

            