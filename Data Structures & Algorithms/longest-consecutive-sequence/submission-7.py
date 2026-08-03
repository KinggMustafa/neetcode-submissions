class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        res = 0
        for num in nums:
            if (num-1) not in setnums:
                curr = 1
                while (num+1) in setnums:
                    setnums.remove(num+1)
                    curr += 1
                    num += 1
                res = max(curr, res)
        return res

        