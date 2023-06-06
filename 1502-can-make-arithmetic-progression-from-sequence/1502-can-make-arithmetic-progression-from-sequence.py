class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) ==2:
            return True
        
        sortedArray=sorted(arr)
        result=sortedArray[1]-sortedArray[0]
        
        for i in range(2,len(sortedArray)):
            if result!=sortedArray[i]-sortedArray[i-1]:
                return False  
            
        return True
            