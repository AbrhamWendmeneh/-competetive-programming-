class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum=[nums[0]]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            prefix_sum.append(nums[i])
        return prefix_sum