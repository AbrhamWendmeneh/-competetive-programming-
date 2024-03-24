class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        set_val = set()
        
        for i in nums:
            
            if i in set_val:
                
                return i
            
            else:
                
                set_val.add(i)