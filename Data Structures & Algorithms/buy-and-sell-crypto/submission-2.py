class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #optimal solution
        #this new solution is the same complexity but gets rid of the redundant work of the left pointer from before
        profit = 0
        minimum = float('INF')
        for num in prices:
            #each val we either sell or it becomes our new minimum
            minimum = min(num, minimum)
            profit = max(profit, num - minimum) 
        return profit

        