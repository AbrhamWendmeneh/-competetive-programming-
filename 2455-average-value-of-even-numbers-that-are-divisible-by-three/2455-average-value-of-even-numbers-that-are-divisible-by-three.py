class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=0
        count=0
        for i in nums:
            if i %6==0:
                a+=i
                count+=1
            else:
                continue
        if count==0:
            return 0
        return a//count
        