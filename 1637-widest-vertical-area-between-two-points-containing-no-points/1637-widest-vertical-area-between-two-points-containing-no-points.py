class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        
        max_val = 0
        
        for i in range(1,len(points)):
            
            max_val = max(max_val , points[i][0] - points[i-1][0])
            
        return max_val