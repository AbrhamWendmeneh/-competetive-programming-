class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dict_val = {}
        
        for val in arr:
            
            if val in dict_val:
                
                dict_val[val] +=1
                
            else:
                
                dict_val[val] = 1
                
        result = []        
                
        for i in dict_val:
            
            result.append(dict_val[i])
            
        return len(result) == len(list(set(result)))
            
                
        