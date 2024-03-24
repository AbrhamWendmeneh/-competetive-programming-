class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
            pointer2 +=1
        