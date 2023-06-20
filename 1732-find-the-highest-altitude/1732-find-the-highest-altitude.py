class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
     
        res=[i for i in range(len(gain))]
        accumulator = 0 
        for i in range(len(gain)):
            accumulator += gain[i]
            res[i]=accumulator    
        res=res+[0]
        return max(res)
            