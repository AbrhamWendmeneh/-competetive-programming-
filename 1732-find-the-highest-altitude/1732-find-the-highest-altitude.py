class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        height = 0
        
        temp = 0 
        
        for i in gain:
            
            temp += i
            
            height = max(height, temp)
            
        return height
        