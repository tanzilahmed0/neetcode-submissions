class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        # We can use a hash map to store the current frequencies of the characters in the substring 
        # We can keep iterating through the loop until the count of the least frequent character reaches 
        # k. Then we remove the element that's leaving and decrement the count by one. 
        # Or we check if the window_length - max of the values is greater than k

        left = 0 
        maxLength = 0 
        maxChar = 0
        freqs = {}

        for right in range(len(s)): 
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            maxChar = max(maxChar, freqs[s[right]])
            length = right - left + 1
            # {A: 4, B: 2}
            
            if length - maxChar > k: 
                freqs[s[left]] -= 1 
                left += 1 
                length -= 1
            
            maxLength = max(maxLength, length)

        return maxLength
            