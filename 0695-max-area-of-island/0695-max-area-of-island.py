class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited= set()
        max_area=0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] ==1 and (row,col) not in visited:
                    
                    area= self.explore(grid,row,col,visited)
                    max_area=max(max_area,area)
                    
        return max_area
    
    def explore(self,grid, row ,col,visited):
        
        if col<0 or row<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] == 0:
            return 0
        
        if (row, col) in visited:
            return 0
        
        else:
            visited.add((row,col))
            area=1
            
            area +=self.explore(grid,row-1,col,visited)
            area +=self.explore(grid,row+1,col,visited)
            area +=self.explore(grid,row,col-1,visited)
            area +=self.explore(grid,row,col+1,visited)
            return area
        
        
        
    
            
                    