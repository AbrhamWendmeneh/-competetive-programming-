class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        visited=set()
        
        for row in range(len(grid)):
            
            for col in range(len(grid[0])):
                
                if self.explore(grid, row, col, visited)==True:
                    
                    count +=1
                    
        return count
    
    def explore(self,grid, row, col, visited):

        if col<0 or row<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] == "0":
            return False

        if (row,col) in visited:
            
            return False
        else:
        
            visited.add((row,col))

            self.explore(grid,row-1,col,visited)
            self.explore(grid,row+1,col,visited)
            self.explore(grid,row,col-1,visited)
            self.explore(grid,row,col+1,visited)

            return True
        
        
        
            