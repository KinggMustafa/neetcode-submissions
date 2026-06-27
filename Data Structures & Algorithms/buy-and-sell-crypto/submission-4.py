class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = float('INF')
        maxprofit = 0
        for price in prices:
            maxprofit = max(maxprofit, price - minbuy)
            minbuy = min(minbuy, price)
        return maxprofit
        #o(n) time where n is the length of pricee, constant space
