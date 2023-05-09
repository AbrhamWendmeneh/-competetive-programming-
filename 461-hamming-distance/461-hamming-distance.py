class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val= x ^ y
        print(bin(val)[2:])
        return val.bit_count()