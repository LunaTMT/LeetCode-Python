class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        n = len(prices)
        profit = 0
        while r < n:
            current_profit = prices[r] - prices[l]
            
            if prices[l] < prices[r]:
            
                profit = max(current_profit, profit)
            else: 
                l = r
            r += 1
        return profit    
