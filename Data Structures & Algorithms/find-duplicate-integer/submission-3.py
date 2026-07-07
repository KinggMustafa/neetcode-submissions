class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #phase 1, fast moves at 2x speed, and we jump from 1 index, to the index corresponding to that value
        fast = 0
        slow = 0
        while 1:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        slow = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast
        #o(n) time where n is the length of nums, reseting slow makes more sense to me but it is completley symmetric and does not matter
