class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]:
                
                nums[i-1] = nums[i-1] * 2
                nums[i] = 0
                
            else:
                continue
                
        pointer1 = 0
        pointer2 = 0
        
        while pointer1 < len(nums):
            
            if nums[pointer1] == 0:
                
                pointer1 += 1
            
            else:
                
                nums[pointer2] = nums[pointer1]
                pointer1 += 1
                pointer2 += 1
                
        while pointer2 < len(nums):
            
            nums[pointer2] = 0
            pointer2 += 1
            
        return nums
        