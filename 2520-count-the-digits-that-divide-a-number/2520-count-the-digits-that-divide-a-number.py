class Solution:
    def countDigits(self, num: int) -> int:
        counter=0
        # for i in str(num):
        #     if num%int(i)==0:
        #         counter+=1
        # return counter
        i=0
        while i<len(str(num)):
            if num % int(str(num)[i])==0:
                counter+=1
            i+=1
        return counter