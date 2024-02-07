class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        dict_val = {}
        
        for i, val in enumerate(edges):
            
            if val in dict_val:
                
                dict_val[val] += i
            
            else:
                
                dict_val[val] = i
        
        val = sorted([(value, key) for (key,value) in dict_val.items()], reverse = True)
        
        temp_val = val[0][0]
        
        temp_key = val[0][1]
        
        for i in range(1, len(val)):
            
            if temp_val == val[i][0]:   
                
                temp_key = min(val[i][1], temp_key)
      
        return temp_key
                
        