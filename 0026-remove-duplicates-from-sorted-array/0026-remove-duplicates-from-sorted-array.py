class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 1, 1 

        while fast < len(nums):
            if nums[fast] == nums[fast - 1]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
                
        return slow
        