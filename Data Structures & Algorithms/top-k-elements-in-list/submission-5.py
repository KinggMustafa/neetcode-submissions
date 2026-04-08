class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we need to eliminate sorting
        #the most k will ever be is the length of nums
        #count the freq and then sort by grouping that way
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        kfreq = []
        for i in range(len(nums)+ 1):
            kfreq.append([])

        for key, value in freq.items():
            kfreq[value].append(key)
        
        
        output = []
        
        for bucket in range(len(kfreq)-1, -1, -1):
            for value in kfreq[bucket]:
                if len(output) < k:
                    output.append(value)
        return output




                                                                        