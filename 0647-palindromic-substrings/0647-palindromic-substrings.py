class Solution:
    def countSubstrings(self, s: str) -> int:
        
        result = 0
        
        for i in range(len(s)):
            
            j = i+1
            
            while j < len(s)+1:
                
                if s[i:j] == (s[i:j])[::-1]:
                    
                    result += 1
                    
                j += 1
                
        return result 
        