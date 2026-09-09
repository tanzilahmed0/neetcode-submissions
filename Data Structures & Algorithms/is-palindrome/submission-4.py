class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = ''.join(filter(str.isalnum, s))
        
        new_string = new_string.lower()
        
        left = 0
        right = len(new_string) - 1

        while left < right: 
            if new_string[left] != new_string[right]:
                return False
            elif new_string[left] == new_string[right]:
                left += 1
                right -= 1
        
        
        return True

                
            
            
            

        
    

        