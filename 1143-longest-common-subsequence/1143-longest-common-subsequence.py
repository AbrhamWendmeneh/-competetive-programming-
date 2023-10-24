class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        dp= [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1,m+1):
            
            for j in range(1,n+1):
                
                if text1[i-1]==text2[j-1]:
                    
                    dp[i][j]=dp[i-1][j-1]+1
                    
                else:
                    
                    dp[i][j]= max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]
    
    
'''
This is how the dynamic programming works
   |   | 0 | 1 | 2 | 3 | 4 | 5 | 6
-----------------------------------
   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
-----------------------------------
   |   |   |   |   |   |   |   |   | 
-----------------------------------
A  |   |   |   |   |   |   |   |   | 
-----------------------------------
B  |   |   |   |   |   |   |   |   | 
-----------------------------------
C  |   |   |   |   |   |   |   |   | 
-----------------------------------
B  |   |   |   |   |   |   |   |   | 
-----------------------------------
D  |   |   |   |   |   |   |   |   | 
-----------------------------------
A  |   |   |   |   |   |   |   |   | 


and then from the given condition we can do like this one

   |   | 0 | 1 | 2 | 3 | 4 | 5 | 6
-----------------------------------
   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
-----------------------------------
   |   | 0 | 0 | 0 | 0 | 0 | 0 | 0
-----------------------------------
A  |   | 0 | 0 | 0 | 1 | 1 | 1 | 1
-----------------------------------
B  |   | 0 | 1 | 1 | 1 | 2 | 2 | 2
-----------------------------------
C  |   | 0 | 1 | 1 | 2 | 2 | 2 | 2
-----------------------------------
B  |   | 0 | 1 | 1 | 2 | 2 | 3 | 3
-----------------------------------
D  |   | 0 | 1 | 1 | 2 | 2 | 3 | 3
-----------------------------------
A  |   | 0 | 1 | 1 | 2 | 3 | 3 | 3

and finally return the last value form the dp table like the above one which is 3 this is how does dynamic programming works 

'''
                    
                    