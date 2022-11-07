class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[i] + nums[len(nums) - 1 - i] for i in range(len(nums) // 2))
