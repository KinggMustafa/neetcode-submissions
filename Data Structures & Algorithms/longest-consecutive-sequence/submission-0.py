class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sorting will put our consecutive sequences together
        sequence = 1
        longest_sequence = 1
        sorted_nums = sorted(nums)
        for i in range(1,len(sorted_nums)):
            
            if ((sorted_nums[i])-1) == sorted_nums[i-1]:
                sequence += 1
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                sequence = 1
            longest_sequence = max(longest_sequence, sequence)
        return longest_sequence

        #this solution is o(nlogn) where n is the length of nums
        #this solution is o(n) where n is the length of the string worst case 

