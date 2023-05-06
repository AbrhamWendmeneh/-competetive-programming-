class Solution:
    def countBits(self, n: int) -> List[int]:
        val=[]
        for i in range(n+1):
            val.append(i.bit_count())

        return val