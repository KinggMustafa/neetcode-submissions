class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                maxprofit = max(maxprofit, profit)
        return maxprofit
        #o(n^2) solution where n is the length of prices, constant space