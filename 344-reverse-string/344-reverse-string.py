class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse()
        '''
        left=0
        right=len(s)-1
        
        while right>=left:
            
            s[right],s[left]=s[left],s[right]
            
            right-=1
            left+=1'''
        if len(s)==1:
            return s
        else:
            
            return self.reverseString(s[1:]) + s[:1]
       
                
        
