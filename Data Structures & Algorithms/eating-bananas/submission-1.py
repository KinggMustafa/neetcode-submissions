class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kokoeat(k):
            runsum = 0
            for pile in piles:
                runsum += math.ceil(pile / k)
            if runsum <= h:
                return True
            return False

        l = 1
        r = max(piles)
        minres = float('INF')

        while l <= r:
            midpoint = (r + l) // 2
            if kokoeat(midpoint): #if true all vals to the right of midpoint are valid so
                minres = min(minres, midpoint)
                r = midpoint -1
            else:
                l = midpoint + 1
        return minres

        


        