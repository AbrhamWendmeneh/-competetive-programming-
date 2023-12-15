class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        dict_val={}
        
        for i, val in enumerate(paths):
            
            dict_val[val[0]] = val[1]
            

        i = paths[0][0]
        
        while i in dict_val:
            
            i = dict_val[i]
            
        return i
            
                
                
            
        
            
#         print(dict_val)
            
#         return "A"