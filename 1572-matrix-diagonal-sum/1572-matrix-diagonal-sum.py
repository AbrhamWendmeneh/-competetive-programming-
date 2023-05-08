class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        sum2=0
        n=len(mat)
        for i in range(n):
            sum1+=mat[i][i]
            sum2+=mat[i][n-1-i]
        if n%2==0:
            return sum1+sum2
        else:
            return sum1+sum2-mat[n//2][n//2]
        