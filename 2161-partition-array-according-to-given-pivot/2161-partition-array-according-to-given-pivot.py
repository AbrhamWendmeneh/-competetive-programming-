class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        # nums.sort()
        for i in nums:
            if i < pivot:
                a.append(i)
            elif i==pivot:
                c.append(i)
            else:
                b.append(i)
        return a+c+b