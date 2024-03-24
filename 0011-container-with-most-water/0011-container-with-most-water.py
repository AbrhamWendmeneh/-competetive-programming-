class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        pointer1 = 0
        pointer2 = len(height) - 1
        
        result = 0
        
        while pointer1 <= pointer2:
            
            if height[pointer1] < height[pointer2]:
                
                result = max(result, (pointer2 - pointer1)* height[pointer1])
                
                pointer1 += 1
                
            else:
                
                result = max(result, (pointer2 - pointer1)* height[pointer2])
                
                pointer2 -= 1
                
        return result
        
        