class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]

        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            profit = prices[i] - lowest
            maxProfit = max(maxProfit, profit)
        return maxProfit

        

        