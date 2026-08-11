class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #the most k can ever be is the size of the input array
        #if we have a hashmap and count the freq
        res = [[] for i in range(len(nums)+1)]
        ans = []
        freq = defaultdict(int) #at each freq, there can be multiple values i.e there being 2 2's and 2 3's. 
        for num in nums:
            freq[num]+= 1
        
        for key, value in freq.items():
            res[value].append(key)


        for i in range(len(res)-1, -1, -1):
            while res[i] and k:
                ans.append(res[i].pop())
                k -= 1
        return ans


        
        