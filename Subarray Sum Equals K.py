class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0

        prefix = 0

        count = Counter({0: 1})

        for num in nums:

            prefix += num

            ans += count[prefix - k]

            count[prefix] += 1

        return ans
