class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price_index = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_buy_price_index]:
                min_buy_price_index = i
            else:
                profit = prices[i] - prices[min_buy_price_index]
                if profit > max_profit:
                    max_profit = profit

        return max_profit