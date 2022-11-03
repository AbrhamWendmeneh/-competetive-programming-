class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        summ = 0
        nums.sort()
        l = 0
        for r, num in enumerate(nums):
            summ += num
            while summ + k < num * (r - l + 1):
                summ -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans       
