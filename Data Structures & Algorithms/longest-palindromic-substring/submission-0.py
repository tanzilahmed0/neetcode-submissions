class Solution:
    def longestPalindrome(self, s: str) -> str:

        # We can use two pointers and check every index for a possible palindrom 
        # if it's an odd length substring, the center is right in the middle, but if it's even 
        # it's between 2 characters.

        # Odd length palindrome
        longest = ""

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1 
                right += 1 
            # Because we alr moved left and right past, we need to decrement the pointer by 1 
            substring = s[left + 1:right]
            if len(substring) > len(longest): 
                longest = substring

        # Even length palindrome: 
        for i in range(len(s)): 
            left, right = i, i + 1 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1 
                right += 1 
            substring = s[left + 1:right]
            if len(substring) > len(longest): 
                longest = substring

        
        return longest
        
        

        