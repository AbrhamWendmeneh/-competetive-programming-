class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dict_val = {}
        
        result = []
        
        counter = 0
        
        for i in nums:
            
            if i in dict_val:
                
                result.append(i)
                
            else:
                
                dict_val[i] = 1
                
        return result
                