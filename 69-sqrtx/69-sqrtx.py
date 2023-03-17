class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(x**(1/2))
        '''i=0
        while   True:
            if (i+1)*(i+1)>x:
                return i
            i+=1'''
        low=1
        high=x
        if x==0:
            return 0
        while low<=high:
            mid=(low+high)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                low=mid+1
            else:
                high=mid-1
        return low-1