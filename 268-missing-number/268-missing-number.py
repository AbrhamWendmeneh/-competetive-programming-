class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        '''low=nums[0]
        high=[-1]
        while low <=mid:
            mid= (low+high)/2
            if '''
        # for i, j in enumerate(nums):
        #     if j!=i:
        #         return i
        # return len(nums)
        a=[]
        
        
        for i in range(min(nums),len(nums)+1):
            if i not in nums:
                return i
        
        return 0
        ''''
        for i in range(1,len(nums)+1):
            if nums[i]-nums[i-1]==1:
                continue
            else:
            
            if nums[i]-nums[i-1]!=1:
                return nums[i-1]+1
            else:
                return nums[-1]-1'''
            