class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        dict_val = {}
        result = []
        
        for i,val in enumerate(nums):
            
            if i+1 in dict_val:
                
                dict_val[i+1] += 1
            else:
            
                dict_val[i+1] = 0

        for val in nums:
            
            if val in dict_val:
                
                dict_val[val] += 1
    
        
        for i in dict_val:
            
            if dict_val[i] >1:
                
                duplicate = i
                
            elif dict_val[i] == 0:
                
                missing = i
                
        return [duplicate, missing]
        
        