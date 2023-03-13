class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        emp=[]
        emp.append(1)
        for i in range(rowIndex):
            for j in range(i,0,-1):
                emp[j]+=emp[j-1]
            emp.append(1)
        return emp
    
    