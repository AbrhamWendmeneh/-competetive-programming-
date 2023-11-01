class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        nums.sort()
        for i in range(len(nums)-2):
            
            left=i+1
            right=len(nums)-1
            
            
            
            if i > 0 and nums[i]==nums[i-1]:
                continue
                
            while left < right:
                
                val=nums[i]+nums[left]+nums[right]
                
                if val==0:
                    result.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left]==nums[left+1]:
                        
                        left+=1
                        
                    while left < right and nums[right]==nums[right-1]:
                        
                        right-=1
                        
                    left+=1
                    right-=1
                    
                elif val<0:
                    left+=1
                    
                else:
                    right-=1
                    
        return result
