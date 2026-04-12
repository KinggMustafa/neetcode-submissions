class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums) #constant lookup using hashing
        
        if not nums:
            return 0
        
        sequence = 1
        for i in range(len(nums)):
            #how can we tell what the start of a sequence will be
            cursequence = 1
            if nums[i] -1 not in setnums: #we know a sequence has started
                nextnum = nums[i] + 1
                while (nextnum) in setnums:
                    cursequence += 1
                    nextnum += 1
                #once we find a start we have to keep adding
            sequence = max(sequence, cursequence) #keep track of our max sequence
        return sequence

        #the time compexity is o(n) time where n is the length of nums and o(n) space where n is the length of the set of nums 


