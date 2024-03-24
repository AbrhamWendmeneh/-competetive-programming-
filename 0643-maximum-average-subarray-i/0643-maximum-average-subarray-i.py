class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxSum = sum(nums[:k])
        
        result = maxSum
        
        i = k

        while i < len(nums):

            result += nums[i] - nums[i - k]
            
            maxSum = max(maxSum, result)
            
            i += 1

        return maxSum / k