class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n,4).is_integer()
#         if n <1:
#             return False
#         while n%4==0:
#             n/=4
#         return n==1
