class Solution:
    def frequencySort(self, s: str) -> str:
        
        dict_val = {}
        
        result = ""
        
        for i  in s:
            
            if i in dict_val:
                
                dict_val[i] += 1
                
            else:
                
                dict_val[i] = 1
        
        val = sorted([(value,key) for (key,value) in dict_val.items()], reverse = True)
        
        for i in val:
            
            result += (i[0]) * i[1]
                
        return result 
        