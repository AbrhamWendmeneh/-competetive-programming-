class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        expected_sum = n*(n+1)//2
        
        actual_sum = sum(nums)
        
        duplicate = actual_sum - sum(set(nums))
        
        missing_val = expected_sum - actual_sum + duplicate
        
        return [duplicate, missing_val]
        
        
        