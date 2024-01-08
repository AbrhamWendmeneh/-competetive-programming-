class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        result = []
        
        for i in range(len(nums)):
            
            sum_val = 0
            
            for j in range(i, len(nums)):
                
                sum_val += nums[j]
                result.append(sum_val)
  
        result.sort()

        return sum(result[left-1:right])%(7+10**9)
            
            
            
            
            
            
            
            