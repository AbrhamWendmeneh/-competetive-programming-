class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left=0
        
        if nums[left]< nums[-1]:
            
            return nums[left]
        
        right= len(nums)-1
        
        while left < right:
            
            middle= (left+right)//2
            
            if nums[middle] >= nums[right]:
                
                left=middle+1
                
            else:
                
                right=middle
                
        return nums[left]
                