class Solution:
    def hammingWeight(self, n: int) -> int:
        counter=0
        while n:
            counter+= n & 1
            n>>=1
        return counter
                