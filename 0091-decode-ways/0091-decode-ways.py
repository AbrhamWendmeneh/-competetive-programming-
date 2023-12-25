class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0]*(len(s)+1)
        
        dp[0] = 1
            
        for i in range(1, len(s)+1):
            
            val1 = s[i-1:i]
            
            # this is to handle the case where i is 1
            
            if i > 1:
                
                val2 = s[i-2:i]
                
            else:
                
                val2 = None
            
            if int(val1 ) > 0:
                
                dp[i] = dp[i-1]
                
            if val2 and 10 <= int(val2) <= 26:
                
                dp[i] += dp[i-2]
                
        return dp[-1]
                
            