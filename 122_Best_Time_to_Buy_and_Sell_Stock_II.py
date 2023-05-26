class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, value in enumerate(prices[:-1]):
            if value < prices[i+1]:
                profit += (prices[i+1] - value)
        return profit