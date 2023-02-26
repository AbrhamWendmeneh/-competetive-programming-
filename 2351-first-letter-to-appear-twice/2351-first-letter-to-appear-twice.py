class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # for i in range(len(s)):
        # right=1
        # left=0
        # a=[]
        # for i in s:
        #     a.append(i)
        # if len(a)-len(list(set(a)))!=1:
        #     while right<len(s) and right>left:
        #         if s[right]==s[left]:
        #             return s[left]
        #         else:
        #             right+=1
        #             left+=1
        # for i in range(len(s)):
        #     if s.count(s[i])==2:
        #         return s[i] 
        accumulator=[]
        for i in s:
            if i in accumulator:
                return i
            else:
                accumulator.append(i)
        
        
                
            
        
            