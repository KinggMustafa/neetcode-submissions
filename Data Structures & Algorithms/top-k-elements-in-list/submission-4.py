class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        for num in nums:
            freqmap[num] += 1
        #after counting the freq of each number we need to sort based on their key values
        sortfreqmap = sorted(freqmap.items(), key = lambda x: x[1])
        #this says the key for the sorting function will be the second argument in each tuple given which will be the value in our key value pairs
        freqelements = []

        for i in range(len(sortfreqmap)-1, -1, -1):
            if len(freqelements) != k:
                freqelements.append(sortfreqmap[i][0]) #append the key 
        return freqelements
#o(n + m log m) where n is the length of nums, and m is the number of unique entries (length of keys in dictionary)
                                                            

                                                                        