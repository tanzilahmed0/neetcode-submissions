class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        result = []
        left = 0 
        right = len(numbers) - 1 

        while left < right:
            if numbers[left] + numbers[right] > target: 
                right -= 1
            elif numbers[left] + numbers[right] == target: 
                result.extend([left+1, right+1])
                break 
            else: 
                left +=1
            
        
        return result 
        