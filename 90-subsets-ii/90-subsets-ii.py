class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         a=[]
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 a.append(nums[i:j])
                
#             # a.append([nums[]])
        
#         return a
        a=[[]]
        # print(len(a))
        for i in nums:
            for j in range(len(a)):
                b=a[j][:]
                # print(b)
                b.append(i)
                # print(b)
                a.append(sorted(b))
                # print(a)
        val=[]
        for i in a:
            if i not in val:
                val.append(sorted(i))
            else:
                continue
        return val