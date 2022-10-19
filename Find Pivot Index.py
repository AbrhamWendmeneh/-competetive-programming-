class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=[0 for _ in range(n)]
        right=[0 for _ in range(n)]
        for i in range(1,n):
            left[i]=left[i-1]+nums[i-1]
        for j in range(n-2,-1,-1):
            right[j]=right[j+1]+nums[j+1]
        for pos in range(n):
            if left[pos]==right[pos]:
                return pos
        return -1       
