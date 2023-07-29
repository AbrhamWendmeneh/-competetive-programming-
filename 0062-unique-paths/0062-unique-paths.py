class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [['y' for _ in range(n)] for _ in range(m)]
        
        def dp(row,col):
            if row == m-1 and col==n-1:
                return 1
            if memo[row][col] != 'y':
                return memo[row][col]
            # this for the dowm movement of the robot 
            if row+1 < m:
                path1=dp(row+1,col)
                
            # I assign for the parts that are  the row of the edges to be 0
            else:
                path1=0
            
            # this for the right movement of the robot     
            if col+1 < n:
                path2=dp(row,col+1)
                
            # I assign for the parts that are near the col of the edges to be 0
            else:
                path2=0
                
            memo[row][col]= path1 + path2
            return memo[row][col]
        
        return dp(0,0)
                
                
            