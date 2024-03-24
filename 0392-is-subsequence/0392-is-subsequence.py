class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pointer1 = 0      
        pointer2 = 0
        
        check = [0] * len(s)
        
        while pointer1 < len(t) and pointer2 < len(s):
            
            if s[pointer2] == t[pointer1] :
                
                check[pointer2] = 1
                pointer2 += 1
                pointer1 += 1
                
            else:
                
                pointer1 += 1
                
        return check == ([1]*(len(s)))
                
            
                
                