class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set()
        for num in nums:
            if num in setnums:
                return True
            setnums.add(num)
        return False