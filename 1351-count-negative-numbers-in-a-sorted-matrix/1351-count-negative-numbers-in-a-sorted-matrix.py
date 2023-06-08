class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        counter=0
        
        for i in grid:
            
            left=0
            right=len(grid[0])-1
            
            while left<=right:
                
                middle=left+(right-left)//2
                if i[middle] >=0:
                    left=middle+1
                    
                else:
                    right=middle-1
                    
            counter+=len(grid[0])-left
            
        return counter
                    