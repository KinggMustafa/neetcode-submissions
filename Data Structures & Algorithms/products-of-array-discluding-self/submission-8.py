class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(1,len(nums)):
            output[i] = output[i-1] * nums[i-1]
        right = [1] * len(nums)

        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j + 1] * nums[j+1]
            output[j] *= right[j]
        return output

        #optimal o(n) solution with o(n) space