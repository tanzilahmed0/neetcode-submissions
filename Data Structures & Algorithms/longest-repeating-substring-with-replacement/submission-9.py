class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The count of our character is 4 and length of the string is 5
        # 5-4 >= 1 
        # We can do a sliding window where we can keep moving forward 
        # while window length - count of most freq character < k 
        best = 0
        left = 0 
        count = {}
        for right in range(len(s)):                 
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(count.values()) 
            while (right - left + 1) - max_freq > k: 
                count[s[left]] -= 1 
                left += 1
            best = max(right-left+1, best) 
            
        
        return best
                

         