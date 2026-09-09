class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Duplicate signals to me that we should be using a hash set 
        # We can have a sliding window, that also has a while loop that 
        # continues while there is no duplicate characters
        # and then at each step we calculate the length and see if it's greater 
        # than max_length
         
        substring = set()
        max_length = 0 
        left = 0
         
        for right in range(len(s)): 
            

            while s[right] in substring: 
                substring.remove(s[left]) 
                left += 1
            
            substring.add(s[right])

            length = right - left + 1
            max_length = max(max_length, length) 

        return max_length 


        