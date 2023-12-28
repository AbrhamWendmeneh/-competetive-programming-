class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        
        n = len(s)
        
        max_count = 100 
        
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        
        dp[0][0] = 0

        for i in range(1, n + 1):
            
            for j in range(k + 1):
                
                cnt, count = 0, 0

                for l in range(i, 0, -1):
                    
                    if s[l - 1] == s[i - 1]:
                        
                        cnt += 1
                        
                    else:
                        
                        count += 1

                    if j - count >= 0:
                    
                        if cnt >= max_count:
                            
                            cost = 4  
                            
                        elif cnt >= 10:
                            
                            cost = 3  
                            
                        elif cnt >= 2:
                            
                            cost = 2  
                            
                        else:
                            cost = 1 
                            
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - count] + cost)

                if j > 0:
                    
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                    

        return dp[n][k]
