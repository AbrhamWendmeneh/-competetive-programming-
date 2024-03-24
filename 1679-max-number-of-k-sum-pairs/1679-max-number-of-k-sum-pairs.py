class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        pointer1 = 0 
        
        pointer2 = len(nums) - 1
        
        counter = 0
        
        while pointer1 < pointer2:
            
            if nums[pointer1] + nums[pointer2] < k:
                
                pointer1 += 1
                
            elif nums[pointer1] + nums[pointer2] > k:
                
                pointer2 -= 1
            
            else:
                
                counter += 1
                
                pointer1 += 1
                
                pointer2 -= 1
                
        return counter
            