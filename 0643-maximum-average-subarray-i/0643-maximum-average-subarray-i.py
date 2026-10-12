class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window_sum = sum(nums[:k])
        max_val = window_sum
        i = k

        while i < len(nums):

            window_sum += nums[i] - nums[i - k]
            max_val = max(max_val, window_sum)
            i += 1
            
        return max_val / k