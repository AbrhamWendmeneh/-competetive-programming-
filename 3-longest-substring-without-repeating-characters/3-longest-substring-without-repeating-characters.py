class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         sh=set()
#         counter=0
#         for i in s:
#             if i not in sh:
#                 sh.add(i)
#                 counter+=1
            
#         return counter
        chr_set=set()
        start=0
        max_len=0
        for i in range(len(s)):
            while s[i] in chr_set:
                chr_set.remove(s[start])
                start+=1
            chr_set.add(s[i])
            max_len=max(max_len,i-start+1)
        return max_len
                