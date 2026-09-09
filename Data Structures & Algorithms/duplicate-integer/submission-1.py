class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # You can use a hashmap to solve this 

        hash = {}
        for i in nums: 
            if i in hash: 
                return True
            else: hash[i] = True 

        return False

        