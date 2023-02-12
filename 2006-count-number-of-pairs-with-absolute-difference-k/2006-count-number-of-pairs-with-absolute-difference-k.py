class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]-nums[j]==k:
                    a+=1
        return a