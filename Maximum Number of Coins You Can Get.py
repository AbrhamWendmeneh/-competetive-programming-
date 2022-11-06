class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()

        val= 0

        num= len(piles)

        for ind in range(len(piles)//3):

            val += piles[num-(ind+1)*2]

        return val
