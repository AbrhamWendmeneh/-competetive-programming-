class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using bubble sort method with n^2 time complexity
        # for i in range(len(nums)-1,0,-1):
        #     for j in range(i):
        #         if nums[i]<nums[j]:
        #             nums[j],nums[i]=nums[i],nums[j]
        i,a,j=0,0,len(nums)-1
        
        while a<=j:
#             if nums[i]>nums[j]:
#                 nums[j],nums[i]=nums[i],nums[j]
#                 j-=1
#             elif nums[i]< nums[j]:
                
#                 i+=1
#             else:
#                 j-=1
            if nums[a]==0:
                nums[a],nums[i]=nums[i],nums[a]
                
                a+=1
                i+=1

            elif nums[a]==2:
                nums[a],nums[j]=nums[j],nums[a]
                j-=1
            else:
                a+=1

                
                
      
                    
                    
                    
        