class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        cur = sum(nums[:firstLen-1])
        left = [0]*n
        curmax = float('-inf')
        for i in range(firstLen-1, n):
            cur += nums[i]
            curmax = max(curmax, cur)
            left[i-firstLen+1] = curmax
            cur -= nums[i-firstLen+1]
        right = [0]*n
        cur = sum(nums[n+1-firstLen:])
        curmax = float('-inf')
        for i in range(-firstLen,-(n+1),-1):
            cur += nums[i]
            curmax = max(curmax, cur)
            right[i] = curmax
            cur -= nums[i+firstLen-1]
        cur = sum(nums[:secondLen-1])
        res = 0
        for j in range(secondLen - 1, n):
            cur += nums[j]
            if j + 1 - secondLen >= firstLen:
                res = max(res, cur + left[j+1-secondLen-firstLen])
            if n - j - 1 >= firstLen:
                res = max(res, cur + right[j+1])
            cur -= nums[j+1-secondLen]
        return res
        