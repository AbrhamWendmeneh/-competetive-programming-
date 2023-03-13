class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return n > 0 and math.log(n,3).is_integer()
        # return n >0 and (math.log10(n)/math.log10(3)).is_intger()
        '''if n <1:
            return False
        while n%3==0:
            n/=3
        return n==1'''
        if n<=0 and n!=int(n):
            return False
        if n==1:
            return True
        if n>0 and n%3==0:
            return self.isPowerOfThree(n//3)
            