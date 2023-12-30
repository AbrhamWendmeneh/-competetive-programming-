class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        dict_val = {}
        
        n = len(words)
        
        for i, val in enumerate(words):
            
            for j in val:
                
                if j in dict_val:
                    
                    dict_val[j] += 1
                    
                else:
                    
                    dict_val[j] = 1
                    
        for char in dict_val:
            
            if dict_val[char] % n !=0:
                
                return False
            
        return True
                
                    
            