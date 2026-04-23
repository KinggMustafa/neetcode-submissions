class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #we use sorting to our advantage by using two pointers by comparing values and moving the pointers according to the overall sum
        
        output = []
        for i in range(len(nums) -2):

            #outer duplicate check:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) -1
            while left < right:
                overallsum = nums[i] + nums[left] + nums[right]
                if overallsum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: #we need 
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif overallsum < 0:
                    left += 1
                else:
                    right -= 1
        return output


        #time complexity: O(n^2) where n is the length of nums:
        #nlogn for sorting times + o(n) (outer loop ) * o(n) (two pointer while loop)

        #space O(1) since we use .sort() instead of storing a sorted nums