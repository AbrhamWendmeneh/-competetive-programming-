class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        dict_val = {}
        
        for i in nums:
            
            if i in dict_val:
                
                dict_val[i] += 1
            else:
                dict_val[i] = 1
         
        val = sorted([value for (key,value) in dict_val.items()], reverse = True)
        
        result = val[0]
        
        first_val = val[0]
        
        for i in range(1,len(val)):
        
            if first_val == val[i]:

                result += first_val
                
        return result 
      