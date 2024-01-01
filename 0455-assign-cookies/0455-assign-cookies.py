class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        counter = 0
        
        g.sort()
        s.sort()
        
        val1 = 0
        val2 = 0
        
        while val1 < len(g) and val2 < len(s):
            
            if g[val1] <= s[val2]:
                
                val1 += 1
                
            val2 += 1
            
        return val1
            
    
        
        