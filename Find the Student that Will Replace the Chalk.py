class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)

        if k == 0:

            return 0

        for i, c in enumerate(chalk):

            k -= c

            if k < 0:

                return i      
