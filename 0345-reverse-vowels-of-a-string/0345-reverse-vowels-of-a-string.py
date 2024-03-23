class Solution:
    def reverseVowels(self, s: str) -> str:
      
        dict_val = {'a':0,"e":0,"i":0,"o":0,"u":0,'A':0,"E":0,"I":0,"O":0,"U":0}
        
        temp = [ i for i in s if i in dict_val][::-1]
        
        result = ''
        
        j = 0
        
        for i in s:
            
            if i in dict_val:
                
                result += temp[j]
                
                j+=1
                
            else:
                
                result += i
                
        return result
        
        