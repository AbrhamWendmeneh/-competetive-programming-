class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        a=sorted(nums)
#         b=a[1]
#         c=a[1]-a[0]
        
#         for i in range(2,len(nums)):
#             c+=a[i]-b
#         return c  funny code
        b=0
        c=a[len(nums)//2]
        for i in a:
            b+=abs(c-i)
        return b 
            
        