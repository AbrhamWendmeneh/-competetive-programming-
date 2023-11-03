class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        '''
        This question is smilar with question # 1143
        Longest Common Subsequence and I use the same method 
        their difference is that they method of returning between them 
        in this case we can compare to the value of the 
        longest subsquence with the length of the given string 's'
        and if it the same we can simply return True else return False
        
        '''
        
        m, n = len(s), len(t)
        dp= [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1,m+1):
            
            for j in range(1,n+1):
                
                if s[i-1]==t[j-1]:
                    
                    dp[i][j]=dp[i-1][j-1]+1
                    
                else:
                    
                    dp[i][j]= max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1] == m
            