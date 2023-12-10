class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        left=0
        right=1
        val= nums[left]
        max_val=0
        if len(nums)<2:
            return nums[0]
        
        while right< len(nums):
            
            if nums[right] > nums[left]:
                
                val+= nums[right]
                right+=1
                left+=1
                max_val= max(max_val, val)
                
            else:
                max_val= max(max_val, val)
                val= nums[right]
                left+=1
                right+=1
                
        return max_val
            
            