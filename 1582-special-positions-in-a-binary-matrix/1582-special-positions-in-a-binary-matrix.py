class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        counter=0
        
        for i in range(len(mat)):
            
            for j in range(len(mat[0])):
                
                
                if self.possible(i,j,mat) and mat[i][j]==1:
                    
                    counter +=1
                    
        return counter
        
        
    def possible(self, x,y, mat):
        
        for i in range(len(mat)):
            
            if i!=x and mat[i][y]==1:
    
                return False
            
            
        for j in range(len(mat[0])):
            
            if j!=y and mat[x][j]==1:
                
                return False
            
        return True
            
            