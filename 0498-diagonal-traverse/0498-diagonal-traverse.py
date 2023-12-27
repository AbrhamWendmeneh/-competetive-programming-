class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        dict_val = {}
        
        row = len(mat)
        
        col = len(mat[0])
        
        result = []
        
        for i in range(row):
            
            for j in range(col):
                
                if (i+j) in dict_val:
                    
                    dict_val[i+j].append(mat[i][j])
                    
                else:
                    
                    dict_val[i+j] = [mat[i][j]]
                    
        for key in dict_val:
            
            if key%2==0:
                
                dict_val[key] = dict_val[key][::-1]
                
                result += dict_val[key]
                
            else:
                
                result += dict_val[key]
                
        
        
        
                
                    
                    
        
        # return [1,2,4,7,5,3,6,8,9]
        return result
                    