class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         for i in range(len(nums)):
#             if nums[i]==0:
#                 nums.pop(i)
#                 nums.append(nums[i])
#             else:
#                 continue
#         nums[:]=nums
        i = 0

        j = 0

        while j < len(nums):

            if nums[j] == 0:

                j += 1

            else:

                nums[i] = nums[j]

                i += 1

                j += 1

        while i < len(nums):

            nums[i] = 0

            i += 1
                