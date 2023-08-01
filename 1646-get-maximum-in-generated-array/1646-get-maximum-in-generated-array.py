class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {0: 0, 1: 1}  
        
        def dp(val):           
            if val in memo:
                return memo[val]
            if val %2==0:
                memo[val] = dp(val // 2)
            else:
                memo[val]= dp(val//2) + dp((val//2)+1)
            return memo[val]
        
        max_val=0
        # The loop will consider each index i in the generated sequence 
        # from 0 to n and calculate the value at that index 
        # using the dp(i) function
        # and also updates the value if there is new maximium value is found 
        
        for i in range(n+1):
            max_val = max(max_val, dp(i))
            
        return max_val