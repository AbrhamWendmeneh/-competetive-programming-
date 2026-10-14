class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        max_len = 0
        set_val = set()

        while end < len(s):

            while s[end] in set_val:

                set_val.remove(s[start])
                start += 1

            set_val.add(s[end])
            max_len = max(max_len, end - start + 1)
            end += 1
            
        return max_len


        