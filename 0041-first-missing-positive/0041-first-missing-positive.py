class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
        
            if nums[0] == 0:
                
                return 1
            
            elif nums[0] == 1:
                
                return 2
            
        set_val = set(nums)
        
        for i in range(len(nums)):
            
            if i+1 not in set_val:
                
                return i + 1
            
        return len(nums) + 1
            
                
            
            