class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        '''a=[1]
       
        for i in range(rowIndex):
            print(i)
            for j in range(i,0,-1):
                a[j]+=a[j-1]
                print(j)
            a.append(1)
            print(a)
            
            
        return a'''
        
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        
        val=self.getRow(rowIndex-1)
        res=[1]
        for i in range(1,rowIndex):
            res.append(val[i-1]+val[i])
        res.append(1)
        return res
        
        