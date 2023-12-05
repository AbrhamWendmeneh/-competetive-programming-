class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        result=0
        
        temp=n
        
        while temp > 1:
            
            if temp%2==0:
                
                temp= temp//2
                
                result+= temp
                
            else:
                
                temp = (temp-1)//2
                result+= temp+1
                
        return result
        