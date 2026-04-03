class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range (len(nums) + 1)]
        #the highest frequency would be the length of the list
        #the index within the frequency list is their count, and whats in the index is just the number, then pop from the back 
        #store in dictionary first
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            frequency[value].append(key)
        
        top_k = []
        for i in range(len(nums),-1,-1):
            for num in frequency[i]:
                if len(top_k) < k:
                    top_k.append(num)
        return top_k


