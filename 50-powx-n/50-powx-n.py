class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return math.pow(x,n)
#         if x ==1:
#              return 1
#         if n <0:
#              x*=x
#              n=n+1
            
#         while abs(n)>0:
#             x*=x
#             n=abs(n)-1
#         return x
        # return x**n
        if  n== 1:
            return x
        elif (n<0):
            return self.myPow(1/x,-1*n)
            # n=abs(n)
            # x=1/x
        else:    
            if (n%2==0) and n>1:
                # return (self.myPow(x,n/2))*(self.myPow(x,n/2))
                num  = self.myPow(x, n/2)
                return  num * num
            return x* self.myPow(x,n-1)
            
        # else:
        #     for i in range(n+1):
        #         double(x)*=x
        # return x
         
        
    
            
            