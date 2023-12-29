class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        # formula of the brute force approach to find the maximum partition 
        # (n-1)!/(n-k)! * (k-1)!
        
        n = len(jobDifficulty)
        
        if n < d:
            
            return -1
        
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        
        dp[0][0] = 0
        
        for i in range(1, d + 1):
            
            for j in range(1, n + 1):
                
                max_val = 0
                
                for k in range(j-1,-1,-1):
                    
                    max_val = max(max_val,jobDifficulty[k])
                    
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + max_val)
                    
        return dp[d][n]
                
                