class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        left=0
        right=len(nums)-1
        max_val=float('-inf')
        
        while right> left:
            
            max_val= max(max_val,(nums[right]+nums[left]))
            
            left+=1
            right-=1
            
        return max_val