class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val=1
        for i in nums:
            if i ==0:
                return 0
            val*=i
        if val<0:
            return -1
        return 1