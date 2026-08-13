class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        res = 0
        for num in setnums:
            if num-1 not in setnums:
                count = 1
                while (num + 1) in setnums:
                    count += 1
                    num += 1
                res = max(res, count)
        return res
                
                