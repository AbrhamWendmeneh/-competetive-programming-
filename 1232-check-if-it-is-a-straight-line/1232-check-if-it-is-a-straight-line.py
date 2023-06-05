class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2 :
            return True
        valX1,valY1=coordinates[0]
        valX2,valY2=coordinates[1]
        
        resX=valX2-valX1
        resY=valY2-valY1
        
        
        for i in range(2,len(coordinates)):
            
            if (coordinates[i][0]-valX1)*resY!=(coordinates[i][1]-valY1)*resX:
                return False
            
        return True
            
            