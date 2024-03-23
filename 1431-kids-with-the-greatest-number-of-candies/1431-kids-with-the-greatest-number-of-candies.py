class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_val = max(candies)
        
        result = []
        
        for i in candies:
            
            if (i + extraCandies) >= max_val:
                
                result.append(True)
                
            else:
                
                result.append(False)
                
        return result