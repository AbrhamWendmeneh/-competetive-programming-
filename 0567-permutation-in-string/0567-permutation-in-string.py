from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_val1 = defaultdict(int)
        dict_val2 = defaultdict(int)
        n, m = len(s1), len(s2)
        if n > m:
            return False

        for i in s1:
            dict_val1[i] += 1

        left, right = 0, n


        for i in range(left, right):
                dict_val2[s2[i]] += 1

        if dict_val1 == dict_val2:
            return True

        while right < m:
            dict_val2[s2[left]] -= 1
            if dict_val2[s2[left]] == 0:
                del dict_val2[s2[left]]
            left += 1

            dict_val2[s2[right]] += 1
            right += 1

            if dict_val1 == dict_val2:
                return True
            
        return False


            
        