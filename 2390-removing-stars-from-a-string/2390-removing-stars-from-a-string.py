class Solution:
    def removeStars(self, s: str) -> str:
        # a=[]
        # for i in range(len(s)):
        #     a.append(s[i])
        
        b=[]
        for j in s:
            if j=='*':
                b.pop()
            else:
                b.append(j)
        return ''.join(b)
    
        # a=''
        # for k in b:
        #     a+=str(k)
        # return a
                
                