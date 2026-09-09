class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0 

        print(prices[len(prices)-1])

        for i in range(len(prices)): 
            min_price = min(min_price, prices[i])
            if prices[i] < min_price: 
                continue
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            

        return max_profit
        