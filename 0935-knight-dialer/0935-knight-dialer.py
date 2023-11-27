class Solution:
    def knightDialer(self, n: int) -> int:
        
        dp=[1 for _ in range(9)]
  
        if n==1:
            return 10
        
        for _ in range(n - 1):
            dp_new = [0] * 9

            for i in range(9):
                if i == 0:
                    dp_new[i] = dp[4] + dp[6]
                elif i == 1:
                    dp_new[i] = dp[5] + dp[7]
                elif i == 2:
                    dp_new[i] = dp[3] + dp[6]
                elif i == 3:
                    dp_new[i] = dp[2] + dp[7] + dp[8]
                elif i == 4:
                    dp_new[i] = dp[0] + dp[5] + dp[8]
                elif i == 5:
                    dp_new[i] = dp[1] + dp[4]
                elif i == 6:
                    dp_new[i] = dp[0] + dp[2]
                elif i == 7:
                    dp_new[i] = dp[1] + dp[3]
                elif i == 8:
                    dp_new[i] = dp[3] + dp[4]

            dp = dp_new
        return sum(dp)%((10**9)+7)