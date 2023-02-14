class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=[]
#         for i in range(len(nums)):
#             for j in  range(len(nums)-1):
#                 if int(nums[j])> int(nums[j+1]):
#                     nums[j],nums[j+1]=nums[j+1],nums[j]
        
#         return nums[-k]
        for i in nums:
            a.append(int(i))
        a.sort()
        return str(a[-k])
                
       
