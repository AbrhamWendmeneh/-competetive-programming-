class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if set(nums) == {1}:

            return len(nums) - 1

        ans = 0

        last,now = 0,0

        for n in nums:

            if n == 1:

                now += 1

            else:

                ans =max(ans,last + now)

                last = now

                now = 0

        ans = max(ans,last + now)

        return ans 
