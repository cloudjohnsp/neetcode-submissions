class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_buy = 0, prices[0]
        for sell in prices:
            max_profit = max(sell-min_buy, max_profit)
            min_buy = min(min_buy, sell)
        return max_profit
