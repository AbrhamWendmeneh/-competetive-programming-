class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        firstval=0
        tempval=firstval
        
        for i in gain:
            
            firstval+=i
            tempval=max(firstval,tempval)
            
        return tempval
            
        
            