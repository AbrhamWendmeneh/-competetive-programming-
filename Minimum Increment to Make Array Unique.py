class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        steps = 0

        for i in range(1, len(nums)):

            if nums[i] <= nums[i-1]:

                temp = abs(nums[i] - nums[i-1]) + 1

                nums[i] += temp 

                steps += temp

        return steps 
        
