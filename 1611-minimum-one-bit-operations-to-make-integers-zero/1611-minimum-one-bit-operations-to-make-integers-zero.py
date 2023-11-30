class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def helper(n):
            if n==0:
                return 0
            i=0
            while 2**i <=n:
                i+=1
            i-=1
            return (2**(i+1)) - 1- helper((2**i) ^ n)
        return helper(n)