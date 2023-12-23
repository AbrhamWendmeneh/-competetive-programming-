class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        '''
        (0,0)
        (0,1) N
        (1,1) E
        (1,0) S
        (0,0) W  
        
        '''
        
        set_val = set([(0, 0)])
        
        start = (0, 0)
        
        for i in path:
            
            if i == 'N':
                
                start = (start[0], start[1] + 1) 
                
            elif i == 'S':
                
                start = (start[0], start[1] - 1)
                
            elif i == 'E':
                
                start = (start[0] + 1, start[1])
                
            else:
                
                start = (start[0] - 1, start[1])
                
            if start in set_val:
                
                return True
            
            set_val.add(start)
            
        return False
        
        