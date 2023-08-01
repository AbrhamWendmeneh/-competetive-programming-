class Solution:
    def tribonacci(self, n: int) -> int:

        memo={}
        def dp(val):
            if val ==0:
                return 0
            if val == 1 or val == 2:
                return 1
            if val in memo:
                return memo[val]
            memo[val]= dp(val-1)+dp(val-2)+dp(val-3)
            
            return memo[val]
        
        return dp(n)