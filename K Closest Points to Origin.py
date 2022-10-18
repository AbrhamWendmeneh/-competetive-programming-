class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        min_d = 0
        heapq.heapify(ans)
        for pt in points:
            d = pt[0]**2 + pt[1]**2
            heapq.heappush(ans, (-d, pt)) #always push
            if len(ans) > k: #pop when
                heapq.heappop(ans)
        return [y for x, y in ans]
      









