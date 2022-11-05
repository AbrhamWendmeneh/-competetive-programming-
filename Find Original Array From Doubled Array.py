class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        ans = []

        obj = deque()

        for num in sorted(changed):

            if obj and num == obj[0]:

                obj.popleft()

            else:

                obj.append(num * 2)

                ans.append(num)

        return [] if obj else ans 
