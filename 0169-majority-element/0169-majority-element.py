class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict_val = {}
        
        n = len(nums)//2
        
        max_val = float('-inf')
        
        for i in nums:
            
            if i in dict_val:
                
                dict_val[i] += 1
                
            else:
                
                dict_val[i] = 1
                
        for i in dict_val:
            
            if dict_val[i] > n:
                
                return i
            
            
        