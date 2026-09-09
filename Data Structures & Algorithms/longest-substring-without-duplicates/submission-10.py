class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We can use a sliding window to go through the string 
        # We have a left and right pointer 
        # We expand the window my moving the right pointer 
        # Each time we move our right pointer, we update length to max(maxLength, length)
        # when the char is not a duplicate by using a hashset
        # if we find a duplicate, we move our left pointer by one, and remove it from
        # the hash set
        
        duplicates = set()
        maxLength = 0
        left = 0

        for right in range(len(s)): 
            while s[right] in duplicates:
                duplicates.remove(s[left]) 
                left += 1
            length = right - left + 1 
            duplicates.add(s[right])
            maxLength = max(maxLength, length)
        
        return maxLength