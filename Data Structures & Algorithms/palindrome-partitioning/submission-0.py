class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # At each index we need to decide if it's a palindrome 
        # We know that each character is a palindrome 
        # Adding the current char might make it not be a palindrome but there may be a future 
        # char that makes it a palindrome 
        # So we have one path where we just take each inidivual char as a palindrome 
        # and then another one where we keep moving like sliding window esc until it's not a palindrome
        # and then start a new palindrome from that index, but again a future char might make it a palindrome

        # aabaa
        # At each index, we check possible ending positions for the next substring but only if is a partition
        # For example, 'a' is a possible ending position and so is 'aa' and 'aabaa' 
        # So we can use another index j and loop through the following indices and check for next substring
        # and run backtrack from that index, add add substring to path
        # backtrack(i): all valid palindromic substrings starting from i
        # we start the next substring at j + 1 
        # And we've partitioned the whole string once i == len(s)
        output = []
        path = []

        def isPalindrome(l, r): 
            while l <= r: 
                if s[l] != s[r]:
                    return False
                l += 1 
                r -= 1 
            return True

        def backtrack(i): 
            if i == len(s): 
                output.append(path.copy())
                return 
            
            for j in range(i, len(s)): 
                if isPalindrome(i, j): 
                    path.append(s[i:j+1])
                    backtrack(j + 1)

                    path.pop()

        
        backtrack(0)
        return output

        
        


        