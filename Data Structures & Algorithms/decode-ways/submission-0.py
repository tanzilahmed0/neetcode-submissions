class Solution:
    def numDecodings(self, s: str) -> int:

        # U can decode a maximum of a 2 digit number <= 26. So at each digit, you have the choice of 
        # either using that digit or not using that digit but u have to use the digit next iteration 
        # no matter what, unless it's a 0
        # A digit is valid if it doesn't start with a 0, is less than 27 
        # dp[i] is an array of the number of possible ways to decode first i digits
        # 
        
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1 
        
    
        for i in range(1, len(s) + 1):
            # if the current digit is 0, just that 0 can't be a letter 
            if s[i-1] != '0': 
                dp[i] += dp[i-1] 
            
            # Last two digits 
            if i >= 2: 
                if 10 <= int(s[i-2:i]) <= 26: 
                    dp[i] += dp[i-2]

        
        return dp[-1]




        