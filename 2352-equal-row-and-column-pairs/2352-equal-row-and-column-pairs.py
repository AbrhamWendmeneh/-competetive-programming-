class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        counter = 0
        
        result = [] * len(grid[0])
        
        for i in range(len(grid[0])):
            
            temp = []
            
            for j in range(len(grid)):
                
                temp.append(grid[j][i])
                
            result.append(temp)
            
        for i in grid:
            
            for j in result:
                
                if i == j:
                    
                    counter += 1

        return counter
        
                