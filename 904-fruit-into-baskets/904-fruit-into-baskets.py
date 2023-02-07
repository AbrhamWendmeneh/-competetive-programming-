class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        ans = 0

        count = defaultdict(int)

        let = 0

        for rem, tin in enumerate(fruits):

            count[tin] += 1

            while len(count) > 2:

                count[fruits[let]] -= 1

                if count[fruits[let]] == 0:

                    del count[fruits[let]]

                let += 1

            ans = max(ans, rem - let + 1)

        return ans