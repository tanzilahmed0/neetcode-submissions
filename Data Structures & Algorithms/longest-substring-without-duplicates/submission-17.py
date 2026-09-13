class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # What we can do is keep iterating through the string with a for loop. 
        # And then we can use a sliding window that expands as long as the next character is not a duplicate 
        # So what we can do is then have a maxLength and calculate that each time 

        maxLength = 0 
        dupes = set()
        left = 0
        for right in range(len(s)): 
            while right < len(s) and s[right] in dupes: 
                dupes.remove(s[left]) 
                left += 1
            dupes.add(s[right]) 
            maxLength = max(maxLength, (right-left + 1))
            right += 1 
            
        
        return maxLength

        # set = (a, b) 