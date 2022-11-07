class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        list = []

        people = 0

        for num,siz,enf in trips:

            list.append([siz, num])

            list.append([enf, -num])

        list.sort()

        for position,num in list:

            people += num

            if people>capacity:

                return False

        return True


