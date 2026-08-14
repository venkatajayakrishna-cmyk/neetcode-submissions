class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        n = len(prices)
        max_profit = 0
        while r < n:
            profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                max_profit = max(profit, max_profit)
                r += 1
        return max_profit