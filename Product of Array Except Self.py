class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        ans = [1] * n


        for i in range(1, n):

            ans[i] = ans[i - 1] * nums[i - 1]

            suffix = 1 

        for i, num in reversed(list(enumerate(nums))):

            ans[i] *= suffix

            suffix *= num

        return ans
