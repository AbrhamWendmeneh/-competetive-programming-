class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        dict_val = {}
        
        result = 0
        
        for i, val in enumerate(nums):
            
            if val in dict_val:
                
                dict_val[val] += 1
                
            else:
                
                dict_val[val] = 1
      
        for i in dict_val.keys():
     
            if dict_val[i] == 1:
                
                return -1
            
            else:
                
                result += math.ceil(dict_val[i] /3)
            
            
        return result
    
    
    
'''

This the condition in which it fails 
[14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
dict_val = {14: 10, 12: 9}
and in this case we can make it like this one 
for 14: 3, 3, 2 ,2 which counts to 4 and 
for t12: 3, 3, 3 which counts to 3 
and the minimum sum value is 4 + 3 which is 7 not 8


'''
                
            
                
                
                
                