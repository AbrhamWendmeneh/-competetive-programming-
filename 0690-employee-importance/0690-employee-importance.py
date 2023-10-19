"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        store={employee.id : employee for employee in employees}
        queue= []
        queue.append(store[id])
        
        res_imp=0
        
        while queue:
            
            node = queue.pop(0)
            res_imp += node.importance
            
            for i in node.subordinates:
                
                queue.append(store[i])
                
        return res_imp
            