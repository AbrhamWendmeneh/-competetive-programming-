class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        if k == 0:
            return

        self.helper(nums, 0, n - 1)
        self.helper(nums, 0, k - 1)
        self.helper(nums, k, n - 1)        
        
    def helper(self, nums, left, right):

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1