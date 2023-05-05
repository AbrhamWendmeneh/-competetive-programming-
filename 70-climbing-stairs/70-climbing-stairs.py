class Solution:
    @cache
    def climbStairs(self, n: int,save={1:1,2:2}) -> int:
        
        if n in save:
            return n
        else:
            return self.climbStairs (n-1)+ self.climbStairs(n-2)