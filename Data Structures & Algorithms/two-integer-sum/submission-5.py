class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            check = target - nums[i]
            if check in hashmap: 
                return [hashmap[check], i]
            else:
                hashmap[nums[i]] = i
        
        