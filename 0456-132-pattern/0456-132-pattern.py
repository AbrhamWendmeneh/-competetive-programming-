class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
#         i = 0 
#         n = len(nums)
        
#         while i <= n - 3:
            
#             if nums[i] < nums[i+1] and nums[i+1] > nums[i+2] and nums[i] < nums[i+2]:
                
#                 return True
            
#             i += 1
                       
#         else:

#             return False
            
            min_val = float('-inf')
            n = len(nums) 
            peak = n
            
            for i in range(n-1,-1,-1):
                
                if nums[i] < min_val:
                    
                    return True
                
                while peak < n and nums[i] > nums[peak]:
                    
                    min_val = nums[peak]
                    peak += 1
                    
                peak -= 1 
                nums[peak] = nums[i]
                
            return False
                    
