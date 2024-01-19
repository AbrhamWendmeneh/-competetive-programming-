class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
            self.dict_val = {}
        
            min_val = float('inf')
            
            for i in range(len(matrix[0])):
                
                min_val = min(min_val,self.helper(0, i, matrix))
                
            return min_val
                
    def helper(self, row, col, matrix):
        
        if col < 0 or col >= len(matrix):
            
            return 10000
        
        if row == len(matrix) - 1:
            
            return matrix[row][col]
        
        if (row, col) not in self.dict_val:
            
            self.dict_val[(row, col)] = min(
                self.helper(row+1, col, matrix), 
                self.helper(row+1, col+1, matrix), 
                self.helper(row + 1, col - 1, matrix)) + matrix[row][col]
            
        return self.dict_val[(row, col)]
        
        