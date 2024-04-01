class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        a=len(board)
        b=len(board[0])
        
        def checkIsTrue(row, col):
            
            if not (0 <= row < a and 0 <= col < b ):
                
                return False
            
            if board[row][col] == 'O':
                
                return True
            
            return False
        
        def dfs(row, col):
            
            if checkIsTrue(row, col):
                
                board[row][col] = "1"
                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
                
        for i in range(a):
            
            if board[i][0] == 'O':
                
                dfs(i,0)
                
        for i in range(a):
            
            if board[i][-1] == 'O':
                
                dfs(i, b - 1)
                
        for j in range(b):
            
            if board[0][j] == 'O':
                
                dfs(0,j)
                
        for j in range(b):
            
            if board[-1][j] == 'O':
                
                dfs(a-1, j)
                
        for i in range(a):
            
            for j in range(b):
                
                if board[i][j] == '1':
                    
                    board[i][j] = 'O'
                
                elif board[i][j] == 'O':
                    
                    board[i][j]= 'X'
                
                
            