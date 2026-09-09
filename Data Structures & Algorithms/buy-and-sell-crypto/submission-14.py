class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0 

        left = 0

        for right in range(len(prices)): 
            min_price = min(min_price, prices[right]) 
            profit = prices[right] - min_price 
            max_profit = max(profit, max_profit) 

        return max_profit
            
        