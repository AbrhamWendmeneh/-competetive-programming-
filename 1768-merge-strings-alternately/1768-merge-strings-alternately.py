class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ''
        i = 0
        
        while i < len(word1) and i < len(word2):
            
            result += word1[i]
            
            result += word2[i]
            
            i += 1
            
        if i < len(word1):
            
            result += word1[i:]
            
        if i < len(word2):
             
            result += word2[i:]
            
        return result
        