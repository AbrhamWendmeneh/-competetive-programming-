class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        this is so much intersting to do I like this problem
        it makes me to develop the game using React and also python 
        I will update it when I finish my game
        
        '''
        def solve(board):
            for i in range(9):
                for j in range(9):

                    if board[i][j]=='.':
                        for val in range(1,10):
                            val=str(val)
                            if self.possible(board,i,j,val):

                                board[i][j] = val

                                if solve(board):
                                    return True
                                board[i][j]='.'
                        return False
            return True
        
        return solve(board)             
                
    def possible(self, board,y,x,n):
        
        for i in range(9):
            
            if board[y][i]==n:
                return False
       
            
            if board[i][x]==n:
                return False
            
        # this is for the sub-grids which are 3X3
        xi= (x//3)*3
        yi= (y//3)*3
        
        for i in range(3):
            for j in range(3):
                
                if board[yi+i][xi+j]==n:
                    return False
        return True
    
        