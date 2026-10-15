from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        if len(p) > len(s):
            return []

        result = []
        start, end = 0, len(p)
        p_count = defaultdict(int)
        window_count = defaultdict(int)

        for i in p:
            p_count[i] += 1

        for i in s[start:end]:
            window_count[i] += 1 
        
        if window_count == p_count:
            result.append(start)

        while end < len(s):
            window_count[s[start]] -= 1
            
            if window_count[s[start]] == 0:
                del window_count[s[start]]

            window_count[s[end]] += 1
            start += 1
            end += 1     
            if window_count == p_count:
                result.append(start)       

        return result


        