class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kfreq = []
        for i in range(len(nums)-1, -1, -1): #start, stop, step so traverse backward
            if nums[i] not in kfreq:
                kfreq.append(nums[i])
            if len(kfreq) == k:
                return kfreq
        

            