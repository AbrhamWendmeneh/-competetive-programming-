class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums)==len(list(set(nums))):
#             return False
#         else:
#             nums.sort()
#             for i in range(1,len(nums)):
#                 if nums[i]==nums[i-1]:
#                     return True



#             return False
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
        