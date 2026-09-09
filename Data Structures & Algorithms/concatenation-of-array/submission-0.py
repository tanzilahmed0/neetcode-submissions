class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * (2*n) 

        # We can have one pointer at the start of n, and another at n+1 in ans
        # 

        left, right = 0, n 

        for i in nums: 
            ans[left] = i 
            ans[right] = i  
            left += 1 
            right += 1 

        return ans