class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=0
        d=0
        for i in nums:
            if i>0:
                a.append(i)
            else:
                b.append(i)
        ans=[]
        for i in range(len(nums)//2):
            
            ans.append(a[i])
            ans.append(b[i])
        return ans
        