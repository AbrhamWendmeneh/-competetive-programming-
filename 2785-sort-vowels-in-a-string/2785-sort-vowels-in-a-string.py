class Solution:
    def sortVowels(self, s: str) -> str:
        
        collector=[]
        
        dec= { 'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        
        for char in s:
            
            if char in dec:
                
                collector.append(char)
                
        collector.sort()
        
        result=[]
        
        for char in range(len(s)):
            
            if s[char] in dec:
                
                val=collector.pop(0)
                
                result.append(val)
                
            else:
                
                result.append(s[char])
            
            
        return ''.join(result)
        