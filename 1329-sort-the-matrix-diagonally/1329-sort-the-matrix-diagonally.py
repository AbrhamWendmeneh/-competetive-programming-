class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        row = len(mat)
        
        col = len(mat[0])
        
        dict_val = {}
        
        # this is so as to build dictionary 
        # based on the patter which we have get from the matrix
        # so as to store the values 
        
        for i in range(row):
            
            for j in range(col):
                
                if i - j in dict_val:
                    
                    dict_val[i-j].append(mat[i][j])
                    
                else:
                    
                    dict_val[i-j] = [mat[i][j]] 
                    
        # this is so as to sort the values of dictionary 
        
        for i in dict_val:
            
            dict_val[i] = sorted(dict_val[i])
            
        # based on the sorted values we adjust the value of the former matrix
        # to fit to the question that we have been asked
            
        for i in range(row):

            for j in range(col):

                if dict_val[i - j]:

                    mat[i][j] = dict_val[i-j].pop(0)

          
        return mat
 