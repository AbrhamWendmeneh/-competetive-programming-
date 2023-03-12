class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''a=[]
        for i in s:
            if i not in a:
                a.append(i)
            
        c=''
        a.sort()
        for j in a:
            c+=j
        return c
        right=0
        left=0
        emp=[]
        set_v=set()
        while right<len(s):
            if right not in set_v:
                set_v.add(s[right])
                right+=1
            a=''
            b=[]
            for i in set_v:
                a+=i
            b.append(a)
            
            
            right=left+1
            left+=1
        return ''.join(b)'''
        
        val = []   
        for i in range(len(s)):
            if s[i] in val: 
                continue   
            while val:
                if val[-1] > s[i] :
                    if val[-1] in s[i+1:]: 
                        val.pop()
                    else:
                        break
                else:
                    break
            val.append(s[i])  
            
        return "".join(val)
            
                
        
        
                