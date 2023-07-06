class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        if target==0:
            return len(nums)
        if target <0:
            return -1
        left=0
        currsum=0
        minop=float(inf)
        
        for i in range(len(nums)):
            currsum +=nums[i]
            while currsum > target and i >= left:
                currsum -=nums[left]
                left+=1
            if currsum ==target :
                minop=min(minop,len(nums) - (i-left+1))
        if minop == float(inf):
            return -1
        return minop
        
        