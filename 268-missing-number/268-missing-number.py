class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        '''        
        value=0
        for i in range(len(nums)):
            
            value^=i^nums[i]

            
        return value^(len(nums))'''
        
        value=len(nums)
        for i in range(len(nums)):
            value^=i^nums[i]
        return value
        
        
        
        
        
        

            