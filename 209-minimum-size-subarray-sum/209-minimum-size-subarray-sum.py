class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         i=0
#         val=0
#         j=float('inf')
#         for a in range(len(nums)):
#             val+=nums[a]
#             while val>=target:
#                 j=min(a-i+1,j)
                
#                 val-=nums[i]
#                 i+=1
#         if j==float(inf):
#             return 0 
#         else: return j
        left=0
        val=len(nums)+1
        sumTotal=0
        for i in range(len(nums)):
            sumTotal+=nums[i]
            while sumTotal>=target:
                val=min(i-left+1,val)
                sumTotal-=nums[left]
                left+=1
        if len(nums)+1==val:
            return 0
        return val
                