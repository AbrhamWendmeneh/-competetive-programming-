class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(x**(1/2))
        i=0
        while   True:
            if (i+1)*(i+1)>x:
                return i
            i+=1