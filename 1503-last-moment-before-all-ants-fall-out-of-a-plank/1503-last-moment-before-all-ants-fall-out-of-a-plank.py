class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res=0
        for i in left:
            res=max(res,i)
        for j in right:
            res= max(res, n-j)
        return res