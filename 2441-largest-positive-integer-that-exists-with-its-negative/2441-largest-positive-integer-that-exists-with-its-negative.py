class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if -i in nums and i >0:
                a.append(i)
        if a==[]:
            return -1
        return max(a)
                