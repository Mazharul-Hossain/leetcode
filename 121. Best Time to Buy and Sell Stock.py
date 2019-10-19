class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n^2 complexity Status: Time Limit Exceeded
        # max_profit = 0
        # if prices in None or len(prices) < 2:
        #     return max_profit
        # for i in range(1, len(prices)):
        #     for j in range(i):
        #         if (prices[i] - prices[j]) > max_profit:
        #             max_profit = prices[i] - prices[j]
        # return max_profit

        if len(prices) < 2:
            return 0
        buy_price = prices[0]  # find the minimum
        max_profit = 0         # find the maximum
        for i in range(1, len(prices)):
            if max_profit < (prices[i] - buy_price):
                max_profit = prices[i] - buy_price
                        
            if buy_price > prices[i]:
                buy_price = prices[i]
            

        return max_profit