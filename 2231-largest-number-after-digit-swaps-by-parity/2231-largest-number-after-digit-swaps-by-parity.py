class Solution:
    def largestInteger(self, num: int) -> int:
        
        a=[]
        b=[]
        c=0
        d=0
        
        
        for i in str(num):
            if int(i)%2==0:
                a.append(i)
            else:
                b.append(i)
       
        a=sorted(a)
        a=a[::-1]
        b=sorted(b)
        b=b[::-1]
        
        ans=[]
        
        
        for i in str(num):
            if int(i) %2==0:
                ans.append(int(a[c]))
                c+=1
            else:
                ans.append(int(b[d]))
                d+=1
        final=''        
        for i in ans:
            final+=str(i)
        return int(final)