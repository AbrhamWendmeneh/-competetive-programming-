class Solution:
    def maxScore(self, s: str) -> int:
        
        inc = 1
        
        res1 = 0
        
        res2 = 0
        
        max_val = 0
        
        while inc <= len(s)-1:
            
            res1 = s[:inc].count('0')
            
            res2 = s[inc:].count('1')
            
            max_val =max(max_val, res1 + res2)
            
            inc +=1
            
            
        return max_val
            
            