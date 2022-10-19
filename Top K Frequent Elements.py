class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        bag = {}
        for elt in nums:
            if elt not in bag:
                bag[elt] = 1
            else:
                bag[elt] += 1       
       # Index of array = frequencies

        freq = [[] for i in range(len(nums) + 1)]       
        for key, val in bag.items():
            freq[val].append(key)       
        res = []
        i, n = 0, len(freq)
        while i < n and k != 0:
            if len(freq[n-1-i]) > 0:
                res += freq[n-1-i]
                k -= len(freq[n-1-i])
            i += 1
        return res  
