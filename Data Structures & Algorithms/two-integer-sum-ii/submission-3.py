class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # We can have two pointers, one on the left and one on the right 
        # We check if the left + right is equal to the target. 
        # If it's greater than the target, we know we have to move the right pointer left 
        # and if it's less than the target, we have to move the left pointer left 

        result = []
        l, r = 0, len(numbers) - 1 
        while l < r: 
            total = numbers[l] + numbers[r]
            if total == target: 
                result.append(l+1)
                result.append(r+1)
                break
            elif total < target: 
                l += 1 
            else: 
                r -= 1 
        
        return result