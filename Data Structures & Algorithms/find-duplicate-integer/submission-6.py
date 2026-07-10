class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #phase 1
        slow = 0
        fast = 0
        while (1):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        #if slow and fast are equal reset 1 pointer then increment until they are equal
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        #o(n) time with constant space
        