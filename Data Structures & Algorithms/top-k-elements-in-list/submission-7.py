class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, value in freq.items():
            bucket[value].append(key)
       
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if k and bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    k -= 1
        return res
