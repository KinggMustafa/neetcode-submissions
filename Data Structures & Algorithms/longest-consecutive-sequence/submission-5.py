class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if you keep everything in a set and do lookups its o(1)
        #the only way we know its the start of a sequence is it 
        setnums = set(nums)
        best = 0
        for num in setnums:
            if num-1 not in setnums:
                sequence = 0
                start = num
                while start in setnums:
                    sequence += 1
                    start += 1
                best = max(sequence, best)
        return best
        #this is o(n) because if the while loop ever ran for the length of nums no other iteration would
        #this is why we loop over setnums just in case our len(nums) sequence has a duplicate
        #o(n) space where n is the length of non duplciate entries in nums
