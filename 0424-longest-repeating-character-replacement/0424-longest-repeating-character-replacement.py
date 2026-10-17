from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right, max_freq, max_len = 0, 0, 0, 0 
        dict_val = defaultdict(int)

        while right < len(s):
            dict_val[s[right]] += 1
            max_freq = max(max_freq, dict_val[s[right]])

            while (right - left + 1) - max_freq > k:
                dict_val[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
            
        return max_len

        