class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # if len(nums)==1:
        #     return nums[0]
        # max_total=0
        # for i in range(len(nums)-k+1):
        #     total=sum(nums[i:i+k])
        #     max_total=max(max_total,total)
        # return max_total/k
        if len(nums)<k:
            return 0
        total=sum(nums[:k])
        max_total=total
        for i in range(len(nums)-k):
            total-=nums[i]
            total+=nums[i+k]
            max_total=max(max_total,total)
        return max_total/k
            