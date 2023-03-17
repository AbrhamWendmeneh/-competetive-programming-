class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#         if target not in nums:
#             return [-1,-1]
        
#         # for target in nums:
#         #     a.append(nums.index(target))
#         #     a.append(nums.index(target)+1)
#         #     break
#         # return a
#         elif len(nums)==1:
#             return [0,0]
#         a=[]
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 a.append(i)
#                 if nums.index(nums[i+1]) < len(nums) and nums[i+1]==target:
#                     a.append(i+1)
#                 else:
#                     a.append(i)
#                 break
#             elif nums[i]==target:
#                 a.append(i)
#                 a.append(i)
#                 break
#         return a
        '''a=[]
    
        for i in range(len(nums)):
            
            if nums[i]==target:
                
                a.append(i)
                
        if len(a)==0:
            
            return [-1,-1]
    
        c,d=min(a),max(a)
        
        return (c,d)'''
        right=len(nums)-1
        left=0
        a=[]
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            # elif nums[mid]>target:
            else:
                right=mid-1
            '''else:
                a.append(mid)
                
        if len(a)==0:
            
            return [-1,-1]
    
        c,d=min(a),max(a) 
        return (c,d)'''
        val=-1
        if left<len(nums) and nums[left]==target:
            val=left
        if val==-1:
            return [-1,-1]
        
        high=len(nums)-1
        low=0
        while low<=high:
            mid=(high+low)//2
            if (nums[mid])<=target:
                low=mid+1
            # elif nums[mid]>target:
            else:
                high=mid-1
        return (val,low-1)
        
                        
        
                