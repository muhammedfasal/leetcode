class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini_price = float('inf')
        max_profit = 0

        for price in prices:
            mini_price = min(mini_price, price)
            max_profit = max(max_profit, price-mini_price)
        return max_profit
        