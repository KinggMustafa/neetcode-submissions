class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #optimal solution
        minimum = float('INF')
        profit = 0
        left = 0
        right = left + 1
        while left < right and right < len(prices):
            if prices[left] < minimum:
                minimum = prices[left]
            profit = max(profit, prices[right] - minimum)
            right += 1
            left += 1
        return profit
            
        #time is o(n) where n is the size of the input array. 