class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        val1=0
        val2=0
        result=0
        
        for i in range(len(points)-1):
            
            val1=(points[i][0]-points[i+1][0])
            val2= (points[i][1]-points[i+1][1])
            
            result+=(max(abs(val1), abs(val2)))
            
        return result