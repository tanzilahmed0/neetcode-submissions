class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # I think we can try every index as the center of a palindrome and check if it's a palindrome 
        # and if it is a palindrome we store that palindrome in a hashmap 
        # so i guess for every substring [left: right+1] we check if the the middle we've already calculated as a subtring 
        # 
        count = 0 
        
        # Odd Length Palindrome 
        for i in range(len(s)): 
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                count += 1 
                left -= 1 
                right += 1 

        for i in range(len(s)): 
            left, right = i, i + 1 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                count += 1 
                left -= 1 
                right += 1 

        return count 