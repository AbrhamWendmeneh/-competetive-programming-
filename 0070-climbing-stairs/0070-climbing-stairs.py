class Solution:
    def climbStairs(self, n: int) -> int:
        
        dict_val = {}
        
        dict_val[1] = 1
        
        dict_val[2] = 2
        
        def helper(n):
        
            if n in dict_val:

                return dict_val[n]

            else:

                dict_val[n] = helper(n-1) + helper(n-2)

                return dict_val[n]
            
        return helper(n)
            
            
            
            
        