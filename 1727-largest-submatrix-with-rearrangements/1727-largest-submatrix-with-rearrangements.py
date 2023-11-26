class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        max_area=0
        rows, cols= len(matrix), len(matrix[0])
        
        for i in range(rows):
            
            for j in range(cols):
                
                if matrix[i][j]!= 0 and  i > 0:
                    
                    matrix[i][j]+= matrix[i-1][j]
                    
            counter=sorted(matrix[i][:])
            
            for k in range(cols):
                
                max_area= max(max_area,(cols-k)*counter[k])
              
        return max_area