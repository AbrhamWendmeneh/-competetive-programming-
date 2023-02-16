class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter=0
        temp=n
        if n==1:
            return n
        for i in range(1,n+1):
            temp-=i
            if temp>=0:
                counter+=1
                continue
            else:
                break
        return counter
            
        