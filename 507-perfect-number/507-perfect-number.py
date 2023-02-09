class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        c=1
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                
                c+=i+num//i
                # if c > num:
                #     return False
            # else:
            #     continue
        return num==(c)        
        # b=0
        # for h in a:
        #     b+=h
        # return b==num
            