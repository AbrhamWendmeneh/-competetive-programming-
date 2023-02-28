class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # a=[]
        # for i in range(left,right+1):
        #     if i >0 :
        #         for j in str(i):
        #             if and  i%int(j)==0:
        #                 a.append(int(j))
        # return a
        ans = []
        for i in range(left,right+1):
            value = i
            res = True
            if "0" not in str(i):
                while value != 0:
                    val1 = value % 10
                    if i%val1!=0:
                        res = False
                    value = value // 10
                if res: 
                    ans.append(i)
        return ans