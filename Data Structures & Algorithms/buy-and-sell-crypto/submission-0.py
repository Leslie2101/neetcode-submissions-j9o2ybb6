class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = max(profit, prices[i] - bestBuy)
            bestBuy = min(bestBuy, prices[i])
        
        return profit