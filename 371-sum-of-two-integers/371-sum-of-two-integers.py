class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        val=(a & b)<<1
        result= a ^b
        if val&mask==0:
            return result
        else:
            return self.getSum(val,result&mask)
        
            