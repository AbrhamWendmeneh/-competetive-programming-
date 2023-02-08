class Solution:
    def reverseBits(self, n: int) -> int:
        # s=str(n)
        # return int(bin(n)[:1:-1],2)
        # for i in str(n):
        return int('{:032b}'.format(n)[::-1],2)
            