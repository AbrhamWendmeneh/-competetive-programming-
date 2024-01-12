class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        n = len(s)//2
        
        a = s[:n]
        b = s[n:]
        
        dict_val = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        
        counter1 = 0
        counter2 = 0
        
        for i in range(n):
            
            if a[i] in dict_val:
                
                counter1 +=1
                
            if b[-i-1] in dict_val:
                
                counter2 +=1
                
        return counter1 == counter2
            
            
        