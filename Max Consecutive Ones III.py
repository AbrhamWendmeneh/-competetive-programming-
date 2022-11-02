class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        left, right = 0, 0
        if nums[right] == 0:
            k -= 1
        n = len(nums)
        max_length = 0
        for left in range(n):
            while right + 1 < n and ( (k > 0) or nums[right + 1] == 1 ):
                if nums[right + 1] == 0:
                    k -= 1
                right += 1
            if k >= 0:
                max_length = max(max_length, right - left + 1)
            if nums[left] == 0:
                k += 1
        return max_length      
