class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I can compute the product of the entire array then divide
        # it by nums[i]

        i = 0

        total_product = int(1)
        zeros_count = 0

        while i < len(nums): 
            if zeros_count == 2: 
                break;

            if int(nums[i]) == 0: 
                zeros_count += 1
            else: 
                total_product = total_product * int(nums[i])

            
            i+=1 
        print(total_product)

        result = []
        if zeros_count >= 2: 
            return [0] * len(nums)

        elif zeros_count == 1: 
            for i in nums: 
                if i == 0: 
                    result.append(total_product)
                else: 
                    result.append(0) 
        else: 
            for i in nums: 
                new_product = total_product / i 
                result.append(new_product)

        return [int(x) for x in result]
            

        

            


        