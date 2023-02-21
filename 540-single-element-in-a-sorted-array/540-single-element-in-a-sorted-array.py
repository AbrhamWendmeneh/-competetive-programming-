class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        while i <len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
                break
            else:
                i+=2
        return nums[-1]
        
        
        '''i=0
        
        for a in range(1,len(nums)):
            if nums[i]==nums[a] and i < len(nums):
                i+=2
                break
                
            else:
                j=nums[i]
                i+=1
                
        return j
        i=0'''
        