class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0

        initial = 0

        res= len(people) - 1

        people.sort()

        while initial <= res:

            remain = limit - people[res]

            res -= 1

            if people[initial] <= remain:

                initial += 1

            ans += 1

        return ans
