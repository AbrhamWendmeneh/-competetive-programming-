class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=0
        d=0
        
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        ans=[]
        for i in range(len(nums)):
            if i %2==0:
                ans.append(a[c])
                c+=1
            else:
                ans.append(b[d])
                d+=1
        return ans
                
                
        # for i in nums:
        #     if i%2==0:
        #         ans.append(a[c])
        #         c+=1
        #     else:
        #         ans.append(b[d])
        #         d+=1
        # return ans
#         a=[]
#         b=0
#         c=1
#         while b< len(nums):
#             if b%2==0:
#                 if nums[b]%2==0:
#                     a.append(nums[b])
#                 else: 
#                     continue
#             else:
#                 if nums[c]%2!=0:
#                     a.append(nums[c])
                    
#                 else: 
#                     continue
#             b+=1
#         return a
        