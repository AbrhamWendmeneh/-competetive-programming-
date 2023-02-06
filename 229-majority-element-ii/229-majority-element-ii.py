class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # if len(nums)==1:
        #     return nums
        # for i in range(nums):
        #     if len(nums)/3>1 and 
        a=[]
        for i in list(set(nums)):
            if nums.count(i)>(len(nums)/3):
                a.append(i)
        return a