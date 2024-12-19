class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        val_1 = 0
        val_2 = 0 
        result = 0 
        
        for i in range(len(arr)):
            
            val_1 += arr[i]
            val_2 += i
            
            if val_1 == val_2:
                result += 1
                
        return result 
                
        
        