class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        nums = sorted(nums)

        left, right = 0, len(nums) - 1

        while left < right:
            
            if nums[left] + nums[right] == 0:

                return nums[right]
            
            if nums[left] + nums[right] < 0 :

                left += 1
                
            else:

                right -= 1

        return -1
                