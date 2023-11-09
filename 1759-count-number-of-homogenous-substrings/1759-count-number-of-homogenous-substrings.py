class Solution:
    def countHomogenous(self, s: str) -> int:
        
        
        left, right=0,1
        
        count, result=1, 0
        
        while right< len(s):
            
            if s[left]==s[right]:
                count+=1
                left=right
                
            else:
                result+=(count)*(count+1)//2
                count=1
                left+=1
            right+=1
            
        result+=(count)*(count+1)//2
        
        return result%((10**9)+7)
    
    '''
    The approach which I use is that simple math formula on how to count
    number of values= n*(n+1)/2
    
    
    '''
            
        