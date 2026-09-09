class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # What makes the window valid? 
        # length - count of most freq character <= k 
        # When our window is invalid, we want to move our left pointer 
        # and then decrement the count of that character 
        # when it's not invalid, we want increment the count of that chracter
        # and then calculate the length and see if it's the max length 
        # We need a hashmap for this problem to store the char counts

        charCount = {} 
        left = 0
        max_length = 0 

        for right in range(len(s)): 
            charCount[s[right]] = charCount.get(s[right], 0) + 1 
            while (right - left + 1) - max(charCount.values()) > k: 
                charCount[s[left]] -= 1 
                left +=1 
            
            length = right - left + 1 
            max_length = max(max_length, length)

        return max_length
        