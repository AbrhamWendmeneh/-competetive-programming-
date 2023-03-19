class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a = []
        for i in intervals:
            if not a:
                a.append(i)
            else:
                if a[-1][1] < i[0]:
                    a.append(i)
                else:
                    a[-1][1] = max(a[-1][1],i[1])
        return a