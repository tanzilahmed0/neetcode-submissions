class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # WE can say that we do not want to replace the character that appears the most 
        # frequently 
        # We can use a hashmap and a sliding window approach 
        # We get the frequency of the current character 
        # we can do k replacements which means there can be k characters that are not the most frequent 
        # So in other words the length of the current substrings - most frequent cannot exceed k
        # So we can keep expanding our window until that happens when it does, we decrement 
        # the count of the character at the left pointer and move left by 1 
        # and we always have a result which is max(result, current substring)

        freqs = {} 
        left, right = 0, 0 
        count = 0 

        while right < len(s): 
            freqs[s[right]] = freqs.get(s[right], 0) + 1 

            most_common = max(freqs.values()) 
            length = right - left + 1
            while length - most_common > k: 
                freqs[s[left]] -= 1 
                left += 1 
                length -= 1 
            
            count = max(length, count)
            right += 1 

        return count