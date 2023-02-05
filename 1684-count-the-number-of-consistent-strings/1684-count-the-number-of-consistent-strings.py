class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        a=0
        
        for i in words:
            
            if not (set(i)) - set(allowed):
                
                a+=1
                
        return a
                