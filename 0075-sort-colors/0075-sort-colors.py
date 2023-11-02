class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right= len(nums)-1
        val=0
        
        while left <= right:
            
            if nums[left]==0:
                
                nums[val],nums[left]= nums[left],nums[val]
                val+=1
                left+=1
                
            elif nums[left]==1:
                     
                left+=1
                
            else:
                nums[right],nums[left]=nums[left],nums[right]
                right-=1
             
        
                
                
      
                    
                    
                    
        