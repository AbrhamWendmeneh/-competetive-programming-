class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # first=0
        # second=0
        # setval=set()
        # counter=1
        # while first <=second and second<len(s):
        #     if s[second] not in setval:
        #         setval.add(s[second])
        #         counter=max(counter,second-first)
        #         second+=1
        #     else:
        #         second+=1
        #         first+=1
        # return counter
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
                