class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #n^2, constant space where n is the lenth of the list prices
        profit = float('-inf')
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curprof = prices[j] - prices[i]
                profit = max(curprof, profit)
        return profit