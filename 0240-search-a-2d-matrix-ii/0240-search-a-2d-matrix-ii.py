class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        visited=set()
        grid=matrix
        
        for row in range(len(grid)):
            
            for col in range(len(grid[0])):
                
                if self.explore(grid, row, col, visited,target):
                   
                    
                    return True
                   
        return False
    
    def explore(self, grid, row, col, visited, target):
        if col < 0 or row < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != target:
            # print((row,col))
            return False

        if (row, col) in visited:
            
            return False
        
        else:

            visited.add((row, col))

            self.explore(grid, row - 1, col, visited, target) 
            self.explore(grid, row + 1, col, visited, target) 
            self.explore(grid, row, col - 1, visited, target) 
            self.explore(grid, row, col + 1, visited, target)
               
            return True

            
