class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit ,b = 0, prices[0]
        for i in range(len(prices)):
            max_profit = max(prices[i]-b, max_profit)
            if prices[i] < b:
                b = prices[i]
                continue
        return max_profit
