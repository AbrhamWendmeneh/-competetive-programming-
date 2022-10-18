class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(len(stones) > 1):
            greatest = max(stones)
            stones.remove(greatest)
            second = max(stones)
            stones.remove(second)
            if greatest - second > 0:
                stones.append(greatest - second)
        if stones:
            return stones[0]
        return 0       
