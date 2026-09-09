class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = "".join(ch for ch in s if ch.isalnum())

        new_string = new_string.lower()

        left, right = 0, len(new_string) - 1 

        while left <= right: 
            if new_string[left] != new_string[right]: 
                return False 
            else: 
                left += 1 
                right -= 1 
        
        return True