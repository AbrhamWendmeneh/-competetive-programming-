class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inDegree = [0]*(n+1)
        for i, j in trust:
            
            inDegree[j]+=1
            inDegree[i]-=1
            
        for val in range(1,n+1):
            
            if inDegree[val]== n-1:
                return val
            
        return -1