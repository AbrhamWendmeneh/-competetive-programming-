class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:

            return []

        sorted_intervals = sorted(intervals, key = lambda x: x[0])

        res = [sorted_intervals[0]]

        for interval in sorted_intervals[1:]:

            if interval[0] <= res[-1][1]:

                res[-1][1]=max(interval[1], res[-1][1])

            else:

                res.append(interval)

        return res      
