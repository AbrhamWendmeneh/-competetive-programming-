class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentval=0
        maxval=float(-inf)
        
        for i in nums:
            
            currentval=max(i,currentval+i)
            
            maxval=max(maxval,currentval)
            
        return maxval