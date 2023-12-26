class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    
        memo = {}
        
        def helper(val, total):
            
            if val == n:
                
                if total == target:
                    
                    return 1 
                
                else:
                    
                    return 0
                
            if total >= target:
                
                return 0
            
            if (val, total) not in memo:
                
                ways = 0
                
                for i in range(1, k + 1):
                    
                    ways += helper(val + 1, total + i)
                    
                memo[(val, total)] = ways
                
            return memo[(val, total)]
        
        return helper(0, 0) % ( 10**9 + 7)