class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        val= 0
        for _ in range(len(nums)):
            if nums[val] == 0:
                nums.pop(val)
                nums.insert(0, 0)
                val += 1
            elif nums[val] == 2:
                nums.pop(val)
                nums.append(2)
            else:
                val += 1
        return
