class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        dict_val = dict()
        for i, val in enumerate(s):
            dict_val[val] = i

        start, end = 0, 0
        result = []

        for i in range(len(s)):
            val = dict_val[s[i]]
            end = max(end, val)

            if end == i:
                result.append(end - start + 1)
                start = i + 1
        return result