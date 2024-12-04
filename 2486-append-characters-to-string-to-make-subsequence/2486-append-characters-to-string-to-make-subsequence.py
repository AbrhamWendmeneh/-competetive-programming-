class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_1 = 0 
        pointer_2 = 0
        
        result = len(t)
        
        while pointer_1 < len(s) and pointer_2 < len(t) and result > 0:
            
            if s[pointer_1] == t[pointer_2]:
                
                result -= 1
                pointer_1 += 1
                pointer_2 += 1
                
            else:
                
                pointer_1 += 1
            
        
        return result 
        