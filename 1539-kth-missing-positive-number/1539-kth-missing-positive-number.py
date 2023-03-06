class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        temp=list(range(1,1001))
        emp=[]
        for i in temp:
            if i not in arr:
                emp.append(i)
        if len(emp)>=k:
            return emp[k-1]
        else:
            return 1000+(k-len(emp))