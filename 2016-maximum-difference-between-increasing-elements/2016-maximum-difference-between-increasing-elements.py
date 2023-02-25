class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # right=len(nums)-1
        # left=0
        
#         for i in range(len(nums),0,-1):
            
#             if 
        # max_val=0
        # while right < len(nums):
        # left=0
        # right=len(nums)-1
        # max_diff=0
        # while right<len(nums) and right > left:
        #     if nums[right]-nums[left]<=0:
        #         left+=1
        #     else:
        #         max_diff=max(max_diff,(nums[right]-nums[left]))
        #         right-=1
        # if max_diff>0:
        #     return max_diff
        # return -1
        # # return max_profit if max_profit>0 else return -1
        # left=0
        # right=1
        # max_diff=0
        # while right<len(nums) and left<right:
        #     if nums[right]-nums[left]>0:
        #         max_diff=max(max_diff,(nums[right]-nums[left]))
        #         left+=1
        #     else:
        #         right+=1
        #         # left=right
        # if max_diff>0:
        #     return max_diff
        # return -1 
        
        left=0
        right=1
        max_val=0
        while right<len(nums) :
            if nums[right]-nums[left]<=0:
                left=right
            else:
                max_val=max(max_val,(nums[right]-nums[left]))
                
            right+=1
        return max_val if max_val>0 else  -1
                
                
            
        