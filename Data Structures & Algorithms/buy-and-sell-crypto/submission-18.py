class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        cheap = float('inf') 
        maxProfit = 0 

        for i in range(len(prices)): 
            cheap = min(cheap, prices[i]) 
            profit = prices[i] - cheap 
            print(profit)
            maxProfit = max(maxProfit, profit)

        return maxProfit

        
        