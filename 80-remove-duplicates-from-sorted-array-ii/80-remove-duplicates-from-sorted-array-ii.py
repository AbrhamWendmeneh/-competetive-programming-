class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(len(nums)):
            if j==0 or i==1:
                i+=1
                continue
            if nums[j]!=nums[i-2]:
                nums[i]=nums[j]
                i+=1
        return i
    