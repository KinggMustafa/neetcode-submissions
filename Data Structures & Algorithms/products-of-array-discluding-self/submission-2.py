class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix = [1,nums[0]] #left side
        suffix = [1] * len(nums) #right side, we need to index
        #suffix[len(nums)-1] = 1
        #suffix[len(nums)-2] = nums[len(nums)-1]
        #above i set up base cases

        #instead of doing those base cases, it would fail for an input size less than 2. this new solution does the same thing as before just a little cleaner
        prefix = [1] * len(nums) 

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        
        for p in range(len(prefix)):
            prefix[p] *= suffix[p]
        return prefix

        
        #this is o(n) space and time, where n is the length of nums