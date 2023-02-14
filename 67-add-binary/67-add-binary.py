class Solution:
    def addBinary(self, a: str, b: str) -> str:
#         for i in a:
#             if int(i)==0:
                
#         for j in b:
#             if int(j)==0:
        # return (bin(a)+bin(b))
        a=(int(a,2))
        b=(int(b,2))
        c=bin(b+a)
        return (c[2:])
                
        