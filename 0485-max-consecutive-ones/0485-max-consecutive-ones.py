class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxVal = 0
        
        counter = 0
        
        for i in range(len(nums)):
            
            if nums[i] == 1:
                
                counter += 1
                
                maxVal = max(maxVal, counter)
                
            else:
                
                counter = 0
                
        return maxVal
            
            