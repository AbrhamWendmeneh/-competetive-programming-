class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        min_val = float('inf')
        left, right = 0, 1

        sum_val = nums[0]
        
        if sum_val >= target:
            return 1

        while right < len(nums):
            sum_val += nums[right]

            while sum_val >= target:
                min_val = min(min_val, right - left + 1)
                sum_val -= nums[left]
                left += 1

            right += 1

        if min_val == float('inf'):
            return 0
        return min_val
        