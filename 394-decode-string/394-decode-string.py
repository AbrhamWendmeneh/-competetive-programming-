class Solution:
    def decodeString(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            if s[i]!=']':
                res.append(s[i])
            else:
                emp_1=''
                while res[-1]!='[':
                    emp_1=res.pop()+emp_1
                res.pop()
                
                emp_2=''
                while res and res[-1].isdigit():
                    emp_2=res.pop()+emp_2
                res.append(int(emp_2)*emp_1)
        return ''.join(res)
        
                
                
                