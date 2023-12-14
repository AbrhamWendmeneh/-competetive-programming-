class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        row = len(grid)
        col = len(grid[0])
        
        onesRow = [0 for _ in range(row)]
        zerosRow = [0 for _ in range(row)]
        
        onesCol = [0 for _ in range(col)]
        zerosCol = [0 for _ in range(col)]
        
    
        for i in range(row):
            
            for j in range(col):
                
                if grid[i][j]==1:
                    onesRow[i] += 1 
                    onesCol[j] += 1
                    
                else:
                    
                    zerosRow[i] += 1 
                    zerosCol[j] += 1
                
        for i in range(row):
            
            for j in range(col):
                
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                
        return grid