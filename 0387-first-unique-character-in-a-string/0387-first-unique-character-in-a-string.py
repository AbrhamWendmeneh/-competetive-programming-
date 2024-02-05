class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict_val = {}
        
        for i in range(len(s)):
            
            if s[i] in dict_val:
                
                dict_val[s[i]] += 1
                
            else:
                
                dict_val[s[i]] = 1
                
        for i in range(len(s)):
            
            if dict_val[s[i]] == 1:
                
                return i
            
        return -1
                