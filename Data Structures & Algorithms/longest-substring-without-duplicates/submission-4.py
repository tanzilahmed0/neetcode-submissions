class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We can use a hash set to store the characters so we get no dupes
        # we'll use a left and right pointer for the sliding window
        # If s[right] is already in the set, we have to remove s[l] from 
        # the set and then increment l until it's not a set 
        # if s[right] isn't in the set, we add it to the set and then calculate 
        # the current length and get the max of it compared to previous one
        if not s: 
            return 0 

        strings = set()
        result = 1

        left, right = 0, 0

        for r in range(len(s)): 
            if s[right] in strings: 
                while s[right] in strings:
                    strings.remove(s[left]) 
                    left +=1 
                strings.add(s[right])
                right += 1
            else: 
                strings.add(s[right])
                print(strings)
                length = len(strings) 
                result = max(length, result)
                right += 1

        return result



         