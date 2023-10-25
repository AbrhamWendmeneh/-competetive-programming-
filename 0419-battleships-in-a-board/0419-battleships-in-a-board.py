class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        count=0
        for row in range(len(board)):
            
            for col in range(len(board[0])):
                
                if self.explore(board, row, col):
                    
                    count+=1
                    
        return count
    
    def explore(self, board, row, col):
        
        if board[row][col]=='X' and (row==0 or board[row-1][col] =='.') and (col==0 or board[row][col-1]=='.'):
            return True
        else:
            return False
        