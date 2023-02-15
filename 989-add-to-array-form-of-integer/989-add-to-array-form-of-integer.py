class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # a=''
        # for i in num:
        #     a+=str(i)
        # b=int(a)+k
        # b=str(b)
        # c=[]
        # for j in b:
        #     c.append(int(j))
        # return c
        a=''
        for i in num:
            a+=str(i)
        b=int(a)+k
        c=[]
        for i in str(b):
            c.append(int(i))
        return c
            