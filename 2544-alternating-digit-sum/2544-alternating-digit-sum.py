class Solution:
    def alternateDigitSum(self, n: int) -> int:
        val=0
        for i in range(len(str(n))):
            if i%2==0:
                val+= int(str(n)[i])
            else:
                val-= int(str(n)[i])
        return val