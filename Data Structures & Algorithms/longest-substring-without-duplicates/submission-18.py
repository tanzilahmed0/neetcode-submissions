class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # We can do a sliding window approach 
        # Where we iterate through the string expanding the window until we hit a duplicate 
        # character, from there we shrink the string and remove the char from the set until a non duplicate 

        dupes = set() 
        left = 0 
        maxLength = 0 
        for right in range(len(s)): 
            while s[right] in dupes: 
                dupes.remove(s[left]) 
                left += 1 
            dupes.add(s[right]) 
            maxLength = max(maxLength, right - left + 1)

        return maxLength
            
