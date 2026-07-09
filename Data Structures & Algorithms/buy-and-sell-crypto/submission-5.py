class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        minday = prices[0]
        for price in prices:
            currsum = price - minday
            best = max(best, currsum)
            minday = min(price, minday)
        return best