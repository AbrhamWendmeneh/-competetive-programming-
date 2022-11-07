class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        num = len(cardPoints)

        sm = sum(cardPoints)

        windowSum = sum(cardPoints[:num - k])

        ans = sm - windowSum

        for i in range(k):

            windowSum -= cardPoints[i]

            windowSum += cardPoints[i + num - k]

            ans = max(ans, sm - windowSum)

        return ans
