class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_val=set(nums)
        
        max_count=0
        
        for i in nums:
            
            if i-1 not in set_val:
                
                curr_val= i
                curr_max=1
                
                while curr_val+1 in set_val:
                    
                    curr_max+=1
                    curr_val+= 1
                    
                max_count=max(max_count,curr_max)
            
        return max_count