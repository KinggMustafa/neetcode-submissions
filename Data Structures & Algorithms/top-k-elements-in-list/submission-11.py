class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        

        res = [[] for i in range(len(nums)+1)]
        for key, value in freq.items():
            res[value].append(key)
        
        

        output = []
        for i in range(len(res)-1,-1,-1):
            if k and res[i]:
                for val in res[i]:
                    output.append(val)
                    k -= 1
            else:
                continue
        return output
        #o(n) time where n is the length of nums, o(n) space