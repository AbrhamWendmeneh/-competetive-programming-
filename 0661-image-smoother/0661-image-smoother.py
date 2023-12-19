class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        # this is real application for the case of converting images to gray scale
        row = len(img)
        
        col = len(img[0])
        
        array = [[0]* col for _ in range(row)]
        
        for i in range(row):
            
            for j in range(col):
                
                result, counter = self.helper(i,j, row, col,img)
                            
                array[i][j] = result // counter
                
        return array     
                
    def helper(self, i,j,row, col, img):
        
        result = 0
        
        counter = 0
        
        for k in (i+1,i-1,i):

            for l in (j+1,j-1,j):

                if 0 <= k < row and 0 <= l < col:

                    result += img[k][l]
                    
                    counter += 1
                    
        return (result,counter)
                
                
                
                