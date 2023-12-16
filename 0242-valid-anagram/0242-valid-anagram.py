from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            
            return False
        
        dict_val = defaultdict(int)
        
        for i in s:
            
            dict_val[i] += 1
        
        for i in t:
            
            if i in dict_val:
            
                dict_val[i] -= 1
                
                if dict_val[i] < 0:
                    
                    return False
            else:
                
                return False
                
        return True
            
        
            