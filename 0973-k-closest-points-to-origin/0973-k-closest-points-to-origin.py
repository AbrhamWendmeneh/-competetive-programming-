class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result = []
        
        solution = []
        
        for i,val in enumerate (points):
            
            temp = (val[0])**2 + (val[1])**2
            
            result.append((temp,i))

        val = sorted(result)
        
        for i in range(k):
            
            indx = val[i][1]
            
            solution.append(points[indx])
            
        return solution
        