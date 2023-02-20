class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a=sorted(nums)
        b=[]
        for i in range(len(nums)):
            
            if a[i]==nums[i]:
                continue
            else:
                b.append(i)
        if b:
            return (max(b)-min(b)+1)
        return 0