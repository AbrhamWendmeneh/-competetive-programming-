class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s=s.strip()
        # initial=0
        # for i in range(len(s)):
        #     if s[i]==" ":
        #         initial=0
        #     else:
        #         initial+=1
        # return initial
        s=s.split()
        counter=0
        for i in s[-1]:
            counter+=1
        return counter
            
                
        