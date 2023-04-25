class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        value=[]
        for i in range(len(nums)):
             value.append((nums[i])**2 )
        return sorted(value)
    