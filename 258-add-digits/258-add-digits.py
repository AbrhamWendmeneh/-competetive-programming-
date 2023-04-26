class Solution:
    def addDigits(self, num: int) -> int:
        sumVal=0
        if num <10:
            return num
        else:
            while num >0:
                sumVal+=num%10
        
                num//=10
            return self.addDigits(sumVal)