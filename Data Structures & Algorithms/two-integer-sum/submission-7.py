class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int) #key: value 
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i
        
        #hashmap = {3: 0}
        

            

