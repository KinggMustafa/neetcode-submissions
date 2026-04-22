class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        while left < right:
            while numbers[left] + numbers[right] > target:
                right -= 1
            while numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [numbers[left], numbers[right]]