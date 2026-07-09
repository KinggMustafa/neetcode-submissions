class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(1,len(nums)):
            output[i] = output[i-1] * nums[i-1]
        suffix = 1
        for j in range(len(nums)-2, -1, -1):
            suffix *= nums[j+1]
            output[j] *= suffix
        return output

        #optimal o(n) solution with o(1) extra space, still o(n) space for the output array