class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min price as infinity so first price is guaranteed to be smaller
        min_price = float('inf')
        max_profit = 0 


        for i in range(len(prices)): 
            # We check if we can set the current price as the minimum 
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            # if the profit of selling on this current day is greater than max profit, 
            # then we update it 
            max_profit = max(max_profit, profit)
            

        return max_profit
        