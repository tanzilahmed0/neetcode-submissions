class Solution:
    def numDecodings(self, s: str) -> int:
        # I don't need to actually decode the letters 
        # At each letter, we can choose to use it or not,
        # if we choose to use it, we need to check if it's less than 27 and if the # of digits is <= 2
        # If it's a new digit and 0 we have to return 
        # If we don't use a digit, we have to use it next 
        # We recursiveley check as dfs(i) = dfs(i+1) + dfs(i+2)
        # dfs(i): Number of ways to decode the string starting at i

        memo = {} 


        def dfs(i):
            if i == len(s): 
                return 1 

            if i in memo:
                return memo[i]

            if s[i] == '0': 
                return 0 

            ways = dfs(i+1)
           

            if i + 1 < len(s) and int(s[i:i+2]) < 27: 
                ways += dfs(i+2) 
            
            memo[i] = ways 

            return ways 

        
        return dfs(0) 
        

        
        
            


            
