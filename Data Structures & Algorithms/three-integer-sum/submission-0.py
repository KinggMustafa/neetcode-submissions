class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        #we use sorting to our advantage by using two pointers by comparing values and moving the pointers according to the overall sum
        
        output = []
        for i in range(len(sorted_nums) -2):

            #outer duplicate check:
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(sorted_nums) -1
            while left < right:
                overallsum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if overallsum == 0:
                    output.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1

                elif overallsum < 0:
                    left += 1
                else:
                    right -= 1
        return output