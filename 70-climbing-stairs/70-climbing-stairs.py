class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        
        
        if n==1 or n==2 :
            
            return n
        
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        
        '''
        a=1
        b=2
        for i in range(2,n):
            c=a+b
            a,b=b,c
        return b'''
            