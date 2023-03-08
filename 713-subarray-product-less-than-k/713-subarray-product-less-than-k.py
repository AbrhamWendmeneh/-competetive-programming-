class Solution: 
    import math
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         val=0
        
#         for i in nums:
            
#             if i < k:
#                 val+=1
#         right=1
#         left=0
#         while right<len(nums):
            
            
            
#             if  math.prod(nums[left:right+1])<k:
#                 val+=1
#                 right+=1
                
#             else:
                
#                 left+=1
#         return val+1
        if k<2:
            return 0
        left=0
        right=0
        val=0
        result=1
        while right<len(nums):
            
            result*=nums[right]
            while result>=k:
                result/=nums[left]
                left+=1
            
            val+=right-left+1
            right+=1
        return val
        
            