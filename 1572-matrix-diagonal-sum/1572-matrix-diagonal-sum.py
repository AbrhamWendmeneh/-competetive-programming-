class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    a+=(mat[i][j])
        b=mat[::-1]
        c=0
        for i in range(len(b)):
            for j in range(len(b)):
                if i==j:
                    c+=b[i][j]
        if len(mat[0])%2!=0:
            return a+c-(mat[(len(mat)//2)][(len(mat)//2)])
        else:
            return a+c