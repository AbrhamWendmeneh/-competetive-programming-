class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
#         a=1
#         # if divisor!=0:
#         if dividend==-2147483648 and divisor==-1 :
#                 return 2147483647
#         if dividend*divisor<0:
#             a=-1
#         dividend,divisor,y=abs(dividend), abs(divisor),0

#         while dividend>= divisor:
#             dividend=dividend-divisor
#             y+=1
#         return y*a
        a=False
        if dividend < 0 or divisor < 0:
            a=True

        if dividend < 0 and divisor < 0:
            a = False
        b = abs(dividend) // abs(divisor)
        if a:
            b = -b

        if dividend==-2147483648 and divisor==-1 :
            return 2147483647
        return b

                