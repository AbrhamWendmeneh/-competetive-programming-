class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=[]
        for i in range(len(matrix[0])):
            v=[]
            for j in range(len(matrix)):
                v.append(matrix[j][i])
            a.append(v)
                
        return a