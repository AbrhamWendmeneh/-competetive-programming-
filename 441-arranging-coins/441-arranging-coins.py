class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''counter=0
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
        return counter'''
        if n==1:
            return 1
        right=n-1
        left=0
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            # val=sum(list(range(1,mid+1)))
            
            val=(mid*(mid+1))/2
            
            if val ==n:
                return mid
            elif val>n:
                right=mid-1
            else:
                left=mid+1
        return left-1
            
            
            
            
        