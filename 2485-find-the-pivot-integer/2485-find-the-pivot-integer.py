class Solution:
    def pivotInteger(self, n: int) -> int:
        a=0
        b=[]
        if n==1:
            return n
        for j in range(1,n+1):
            b.append(j)
        for i in range(1,n+1):
            # a+=i
            # if a in b and a is not 1:
            #     return i
            if sum(b[:i+1])==sum(b[i:]):
                return  i+1
            
        return -1