class Solution:
    def judgeCircle(self, moves: str) -> bool:

        x,y=0,0
        for i in moves:
            if i == 'U' :
                y+=1
            elif i=='R':
                x+=1
            elif i=='L':
                x-=1
            else:
                y-=1
                
        if x==0 and y==0:
            return True
        else:
            return False
