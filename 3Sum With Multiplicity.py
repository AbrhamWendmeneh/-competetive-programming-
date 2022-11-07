class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        mod = 1000000007

        ans = 0

        count = Counter(arr)

        for i, x in count.items():

            for j, y in count.items():

                k = target - i - j

                if k not in count:

                     continue

                if i == j and j == k:

                     ans = (ans + x * (x - 1) * (x - 2) // 6) % mod

                elif i == j and j != k:

                      ans = (ans + x * (x - 1) // 2 * count[k]) % mod

                elif i < j and j < k:

                       ans = (ans + x * y * count[k]) % mod

        return ans % mod
