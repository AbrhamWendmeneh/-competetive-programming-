class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        n  = len(colors)
        
        min_val = 0
        
        for i in range(1,n):
            
            val1 = colors[i-1]
            
            val2 = colors[i]
            
            if val1 == val2:
                
                min_val +=  min(neededTime[i], neededTime[i-1])
                
                neededTime[i] = max(neededTime[i],  neededTime[i-1])
            
        return min_val
                
                