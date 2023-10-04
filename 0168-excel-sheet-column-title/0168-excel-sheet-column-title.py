class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        emp=''
        while columnNumber:
            columnNumber-=1
            emp=chr(columnNumber % 26 + 65) + emp
            columnNumber=columnNumber//26
        return emp
            
            
        