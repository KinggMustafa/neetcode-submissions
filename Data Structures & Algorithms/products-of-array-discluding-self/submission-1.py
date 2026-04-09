class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1,nums[0]] #left side
        suffix = [1] * len(nums) #right side, we need to index
        suffix[len(nums)-1] = 1
        suffix[len(nums)-2] = nums[len(nums)-1]
        #above i set up base cases
        for i in range(2, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
        
        for j in range(len(nums)-3, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        for p in range(len(prefix)):
            prefix[p] *= suffix[p]
        return prefix

        
        #this is o(n) space and time