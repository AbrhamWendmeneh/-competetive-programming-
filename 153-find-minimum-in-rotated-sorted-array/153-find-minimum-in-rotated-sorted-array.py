class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)# but it is not relevant for this question
        left=0
        right=len(nums)-1
        while left <= right:
            middle_term=(left+right)//2
            if nums[middle_term] < nums[right]:
                right=middle_term
            else:
                left=middle_term+1
        return nums[right]