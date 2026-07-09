class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j != i:
                    total *= nums[j]
            output[i] = total
        return output


