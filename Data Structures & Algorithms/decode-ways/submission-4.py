class Solution:
    def numDecodings(self, s: str) -> int:

        # 1012
        # What makes a digit valid? 
        # It cannot start with a 0 
        # If it's not a 0, we can either use it then or we can hold off and use it 
        # for the next call 
        # We can do a dynamic programming approach 
        # At each digit, if we use it, it has to be less than 27, the length can't be more than 2 digits 
        # and it cannot start with a 0
        # dfs(i) will return the number of ways to decode the string starting from index i 

        memo = {}
        def dfs(i): 
            if i == len(s): 
                return 1   
            
            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0
            
            # We use this digit and then move 
            take = dfs(i + 1)
            skip = 0

            if 10 <= int(s[i:i+2]) < 27 and i + 1 < len(s): 
                skip = dfs(i+2)

            memo[i] = take + skip
            return memo[i]
        
        return dfs(0)
