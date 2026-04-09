class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #count our index and value
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[i] = nums[i]

        rollingsum = []
        for j in range(len(nums)):
            val = 1
            for key, value in freq.items():
                if j != key:
                    val*= value
            rollingsum.append(val)
        return rollingsum
        