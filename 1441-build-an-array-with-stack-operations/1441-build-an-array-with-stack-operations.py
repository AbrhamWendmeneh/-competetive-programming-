class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        stack=[]
        result=[]
        i=1
        
        while i<=n:
            
            stack.append('Push')
            result.append(i)
            
            if i not in target:
                stack.append('Pop')
                result.pop()
                
            if result==target:
                return stack
            
            i+=1
            
        return stack
            
        
        '''
        stack=[push,]
        '''
            