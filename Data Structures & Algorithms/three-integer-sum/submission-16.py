class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        res = []
        for i in range(len(sortednums)-2):
            if sortednums[i] > 0:
                return res
            j = i + 1
            k = len(sortednums)-1
            while j < k:
                sublist = sortednums[i] + sortednums[j] + sortednums[k]
                if sublist == 0:
                    lis = [sortednums[i], sortednums[j], sortednums[k]]
                    if lis not in res:
                        res.append(lis)
                    j += 1
                    k -= 1
                elif sublist < 0:
                    j += 1
                else:
                    k -= 1
        return res
