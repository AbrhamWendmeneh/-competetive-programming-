class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        result = 0
        
        val = [0] * (n+1)
        
        val[1] = 1
        
        for i in range(2, n+1):
            
            val[i] =1
            
            for j in range(i-1,0,-1):
                
                if nums[i-1] > nums[j-1]:
                    
                    val[i] = max(val[j]+1, val[i])
                    
        for i in range(1,n+1):
            
            result = max(result, val[i])
        
        return result
