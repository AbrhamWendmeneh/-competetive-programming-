class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dict_val1 = {}
        
        dict_val2 = {}
        
        for i in range(len(s)):
            
            if s[i] not in dict_val1:
                
                dict_val1[s[i]] = t[i]
                
            if t[i] not in dict_val2:
                
                dict_val2[t[i]] = s[i]
                
            if dict_val1[s[i]] != t[i] or dict_val2[t[i]] != s[i]:
                
                return False
            
        return True
            
        